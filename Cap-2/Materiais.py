import math
class dieletrico():
    def __init__(self, start, epsilon, KE):
        self.start = start
        self.epsilon = epsilon
        self.KE = KE
        self.cb = []
    def init(self):
        self.cb = [.5 for i in range(self.KE)]
        for i in range(self.start,self.KE):
            self.cb[i] = self.cb[i]/self.epsilon

class DielCond():
    def __init__(self, start, epsilon, KE, sigma):
        self.start = start
        self.epsilon = epsilon
        self.sigma = sigma
        self.KE = KE
        self.ga = []
        self.gb = []
        self.dt = .01/6e8
        self.epsz = 8.8e-12
    def init(self):
        self.ga = [1. for i in range(self.KE)]
        self.gb = [.0 for i in range(self.KE)]
        print(self.KE)
        for i in range(self.start,self.KE):
            self.ga[i] = 1/(self.epsilon + self.sigma*(self.dt/self.epsz))
            self.gb[i] = self.sigma*(self.dt/self.epsz)
class Cilinder():
    def __init__(self, radius, sigma, epsilon, start, end, size):
        self.radius = radius
        self.sigma = sigma
        self.epsilon = epsilon
        self.start = start
        self.end = end
        self.size = size
        self.ga = []
        self.gb = []
        self.dt = 0.01/6e8
        self.epsz = 8.8e-12
        
    
    def init(self):
        self.ga = [ [1.0 for j in range(self.size)] for i in range(self.size)]
        self.gb = [ [.0 for j in range(self.size)] for i in range(self.size)]
        
        for j in range(self.size):
            for i in range(self.size):
                xdist = self.start - i
                ydist = self.end - j
                dist = math.sqrt(pow(xdist, 2.) + pow(ydist, 2.))
                if (dist <= self.radius):
                    self.ga[i][j] = 1. / (self.epsilon + ((self.sigma * self.dt) / self.epsz))
                    self.gb[i][j] = (self.sigma * (self.dt / self.epsz))
                    
                    
