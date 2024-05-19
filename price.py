import numpy as np
from scipy.stats import norm

class Price:
    S = None
    K = None
    r = None
    sigma = None
    T = None
    b = None
    q = None
    
    def __init__(self, S, K, r, sigma, T, q):
        self.S = S
        self.K = K
        self.r = r
        self.sigma = sigma
        self.T = T
        self.b = r - q
        return    
    
    def d1(self):
        res = (np.log(self.S/self.K) + ((self.b + ((self.sigma**2)/2)) *\
            self.T))/(self.sigma * np.sqrt(self.T))
        return res
    
    def d2(self):
        return self.d1()- (self.sigma * np.sqrt(self.T))
        
    def call(self):
        d1_ = self.d1()
        d2_ = self.d2()
        
        res = (self.S* np.exp((self.b -self.r)*self.T) * norm.cdf(d1_)) - \
            (self.K * np.exp(-self.r * self.T) *\
            norm.cdf(d2_))
        return (round(res, 5))
            
    def put(self):
        d1_ = self.d1()
        d2_ = self.d2()
        
        res= (self.K * np.exp(-self.r * self.T) * norm.cdf(-d2_)) - \
            (self.S * np.exp((self.b - self.r) * self.T) * norm.cdf(-d1_))
    
        return (round(res, 5))
    
    # first-order sensitivity
    def delta(self):
        res = self.d1()
        return (format(res, ".5f")) 
    
    # second-order sensitivity
    def gamma(self):
        res = self.d1() - (self.sigma * np.sqrt(self.T))
        return (format(res, ".5f"))
    