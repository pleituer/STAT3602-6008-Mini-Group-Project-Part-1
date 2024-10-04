class Evalutate():
    def __init__(self, dataset, prior, nparams):
        self.dataset = dataset
        self.T = dataset.T
        self.nfrogs = dataset.nfrogs
        self.posteriors = [None for _ in range(self.T+1)]
        self.posteriors[0] = prior
    def evaluate(self, get_posterior):
        """
        Notes: posterior: (m_T, n_T, t) -> posterior function
        """
        for t in range(1, self.T+1):
            self.posteriors[t] = get_posterior(*self.dataset.get(t), t)