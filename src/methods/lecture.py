import numpy as np
from scipy import integrate
from scipy.special import factorial

def lecture_posterior(mt, nt, t):
    """
    Get posterior given some m_T, n_T, and T

    Prior: 
    - nfrogs ~ Possion(10)
    - P(no true love) = 0.5 [corresponding to nfrog = -1]
    - P(true Love = frog i) = 0.5 / (nfrogs + 1) [nfrog = 0 is chongwen]
    - P(respond|is true Love) = 0.9
    - P(respond|not true Love) = 0
    """
    # prior
    lambda_nfrogs = 10
    p_true_love = lambda i, nfrogs: 0.5 if i == -1 else 0.5 / (nfrogs + 1)
    p_respond = 0.9

    # normalizing constant
    _numerator = lambda_nfrogs * pow(p_respond, t)
    _C = pow(_numerator, nt) * np.exp(_numerator) + integrate.quad(lambda x: (1/(mt+1) + nt/2 + x) * pow(x, nt) * np.exp(x), 0, _numerator)[0]/_numerator

    # posterior
    def poseterior(theta1, theta2, theta3):
        # if not isinstance(theta1, int): raise ValueError(f"theta1 should be an integer, got {theta1} instead")
        theta1 = int(theta1)
        if theta1 < nt or -1 > theta2 or theta2 > theta1 or theta3 < 0 or theta3 > 1: return 0 
        _a = pow(1 - theta3, np.where(1 <= theta2 and theta2 <= nt, 1, 0) + np.where(theta2 == 0, mt, 0))
        _b = pow(_numerator, theta1)/(factorial(theta1 - nt) * pow(theta1 + 1, np.where(0 <= theta2 and theta2 <= theta1, 1, 0)))
        return _a * _b / _C
    
    return poseterior

def lecture_prior(theta1, theta2, theta3):
    if theta1 < 0 or theta2 < -1 or theta2 > theta1 or theta3 < 0 or theta3 > 1: return 0
    theta1 = int(theta1)
    lambda_nfrogs = 10
    return pow(lambda_nfrogs, theta1) * np.exp(-lambda_nfrogs) * np.where(theta2 == -1, 0.5, 0.5 / (theta1 + 1)) / factorial(theta1) 