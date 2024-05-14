import numpy as np
from scipy.stats import norm

class Price:
    S = None
    K = None
    r = None
    sigma = None
    T = None
    
    def __init__(self, S, K, r, sigma, T):
        self.S = S
        self.K = K
        self.r = r
        self.sigma = sigma
        self.T = T
        return    
    
    def d1(self):
        return (np.log(self.S/self.K) + (self.r + ((self.sigma**2)/2) *\
            self.T))/(self.sigma * np.sqrt(self.T))
    
    def d2(self):
        return (np.log(self.S/self.K) + (self.r - ((self.sigma**2)/2) *\
            self.T))/(self.sigma * np.sqrt(self.T))
        
    def call(self):
        d1_ = self.d1()
        d2_ = self.d2()
        
        res = self.S*norm.cdf(d1_) - (self.K * np.exp(-self.r * self.T) *\
            norm.cdf(d2_))
        return (format(res, ".5f"))
            
    def put(self):
        d1_ = self.d1()
        d2_ = self.d2()
        
        res= self.S*norm.cdf(d1_) - (self.K * np.exp(-self.r * self.T) *\
            norm.cdf(d2_))-(self.S-self.K*np.exp(-self.r*self.T))
        return (format(res, ".5f"))