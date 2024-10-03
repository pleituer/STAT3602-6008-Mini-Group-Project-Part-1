import numpy as np

class Dataset():
    def __init__(self):
        self.T = -1
        self.cum_nt = np.empty(0)
        self.cum_mt = np.empty(0)
        self.nt = np.empty(0)
        self.mt = np.empty(0)
        self.nfrogs = -1 # not including chongwen
    def set_data(self):
        self.T = 15
        cum_nt = [0, 1, 1, 1, 2, 4, 4, 5, 7, 8, 10, 12, 14, 15, 15, 15]
        cum_mt = [0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 3, 4, 4]
        self.cum_nt = np.array(cum_nt)
        self.cum_mt = np.array(cum_mt)
        self.nt = np.diff([0] + cum_nt)
        self.mt = np.diff([0] + cum_mt)
        self.nfrogs = cum_nt[-1]
        assert len(self.mt) == self.T+1, "Error: set_data() gone wrong, length of mt is not T"
        assert len(self.nt) == self.T+1, "Error: set_data() gone wrong, length of nt is not T"
    def get(self, t):
        return self.cum_mt[t], self.cum_nt[t]