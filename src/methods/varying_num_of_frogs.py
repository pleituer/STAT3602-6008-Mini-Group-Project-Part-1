import numpy as np
from scipy import integrate
from scipy.special import factorial

lambda_nfrogs = 10
p_love = 0.1
p_send = 0.1
r = 0.5

_sample_size = 100

def varying_frogs_posterior(mt, nt, t):
    """
    Get posterior given some m_T, n_T, and T
    """

    # normalizing constant
    _numerator = (1 - p_send) * (lambda_nfrogs + t * r)
    _p_no_love = 1 - p_love
    _C = pow(_numerator, nt) * np.exp((1 - p_send) * lambda_nfrogs) * (1 + _p_no_love/(mt + 1) + (pow(_p_no_love, 2) + pow(_p_no_love, nt+2))/(2*p_love))

    # posterior
    def poseterior(theta_frogs_0, theta_love, theta_p):
        # if not isinstance(theta1, int): raise ValueError(f"theta1 should be an integer, got {theta1} instead")
        theta_frogs_0 = int(theta_frogs_0)
        if theta_frogs_0 < 0 or 0 > theta_love or theta_p < 0 or theta_p > 1: return 0 
        _a = pow(lambda_nfrogs/(t*r), theta_frogs_0) / factorial(theta_frogs_0)
        _b = pow(1 - p_love, theta_love) * np.where(1 <= theta_love and theta_love <= nt+1, np.where(theta_love == 1, pow(1-theta_p, mt), 1-theta_p), 1) 
        theta_frogs_t_samples = np.random.poisson((1 - p_send)*t*r, _sample_size)
        max_nt_theta_frogs_0 = np.maximum(nt, theta_frogs_0)
        if max_nt_theta_frogs_0 == np.abs(nt-theta_frogs_0): _fact = np.ones(_sample_size, dtype=np.longlong)
        else: 
            _fact = np.prod(np.linspace(theta_frogs_t_samples+np.abs(nt-theta_frogs_0)+1, theta_frogs_t_samples+max_nt_theta_frogs_0, num=max_nt_theta_frogs_0-np.abs(nt-theta_frogs_0)).astype(np.longlong), axis=0)
            #_fact = factorial(theta_frogs_t_samples + max_nt_theta_frogs_0) / factorial(theta_frogs_t_samples + np.abs(nt-theta_frogs_0))
        _d = (pow((1-p_send)*t*r, max_nt_theta_frogs_0) * _fact).mean()
        return _a * _b * _d / _C
    
    return poseterior

def varying_frogs_prior(theta_frogs_0, theta_love, theta_p):
    if theta_frogs_0 < 0 or theta_love < 0 or theta_p < 0 or theta_p > 1: return 0
    theta_frogs_0 = int(theta_frogs_0)
    return pow(lambda_nfrogs, theta_frogs_0) * np.exp(-lambda_nfrogs) * p_love * pow(1-p_love, theta_love) / factorial(theta_frogs_0) 