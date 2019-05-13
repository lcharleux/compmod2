import numpy as np
from scipy import integrate, optimize
import copy



class Distribution:
    """
    Distribution meta class.
    """
    
    def inverse_cdf(self, p, b = 1.e5):
        """
        Finds x at which cdf(x) = p.
        """
        return optimize.brentq(lambda x: self.cdf(x) - p, 0., b)
    
    
    def mean(self, a, b):
        """
        Returns the mean value of the distribution over [a, b]
        """
        return (
            integrate.quad(lambda x: x * self.pdf(x), a, b )[0] /     
            integrate.quad(self.pdf, a, b)[0]) 
    
    
    def discretize(self, N, xmax = 10.):
        """
        Disctretizes the distribution:
        * computes N intervals of cumulated probability each 1/N.
        * on each interval, computes the mean value.
        
        Returns: both
        """
        cp = np.linspace(0., 1., N+1)
        x = np.zeros_like(cp)
        for i in range(1, N):
            x[i] = self.inverse_cdf(cp[i])
        x[-1] = xmax
        xm = np.zeros(N)
        for i in range(N):
            xm[i] = self.mean(x[i], x[i + 1])
        return x, xm    
    
class CompositeDistribution(Distribution):
    """
    A composite distribution class.
    """
    def __init__(self, dists = None, weights = None):
       assert len(dists) == len(weights)
       self.dists = dists
       self.weights = np.array(weights)
    
    def cdf(self, x):
       d = self.dists
       w = self.weights
       out = 0.
       for i in range(len(d)):
           out += d[i].cdf(x) * w[i]
       return out
       
    def pdf(self, x):
       d = self.dists
       w = self.weights
       out = 0.
       for i in range(len(d)):
           out += d[i].pdf(x) * w[i]
       return out
    
    def norm(self):
        return self.weights.sum()
       
    def isnormalized(self):
        return self.norm() == 1.
    
    def normalize(self):
        self.weights /= self.norm()       
    
    
    
class Rayleigh(Distribution):
    """
    Rayleigh distribution
    """
    def __init__(self, s = 1.):
        self.s = s
    
    def pdf(self, x):
        s = self.s
        return  x / s**2 * np.exp(-x**2 / (2 * s**2))
    
    def cdf(self, x):
        s = self.s
        return  1. -  np.exp(-x**2 / (2 * s**2))
    
class Weibull(Distribution):
    """
    Weibull distribution
    """
    def __init__(self, k = 1., l = 1.):
        self.k = k
        self.l = l
    
    def pdf(self, x):
        k, l = self.k, self.l
        return  k / l * (x / l)**(k-1) * np.exp(-(x/l)**k)
    
    def cdf(self, x):
        k, l = self.k, self.l
        return  1. - np.exp(-(x/l)**k)


