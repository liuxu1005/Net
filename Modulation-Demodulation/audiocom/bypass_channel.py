import math
import numpy
import matplotlib.pyplot as p
import graphs
import random

class BypassChannel:
    def __init__(self, noise, lag, h):
        self.noise = noise
        self.lag = lag
        self.h = h
        #DO NOT modify the following lines.
        numpy.random.seed()
        random.seed()

    def xmit_and_recv(self, tx_samples):
        hl = len(self.h)
        leng = len(tx_samples)
        size = 0
        lagv = numpy.zeros(self.lag)
        rlt = numpy.empty_like(tx_samples)
        hv = numpy.array(self.h)

        for i in range(leng):
            if i + hl > leng:
                size = leng - i
            else :
                size = hl
            rlt[i] = numpy.dot(tx_samples[i:i+size], hv[0:size].T) 
            
            
        rlt = numpy.concatenate((lagv,rlt),axis = 1)
        return rlt + numpy.random.normal(0, self.noise, len(tx_samples)+self.lag)
        
        #raise NotImplementedError, "xmit_and_recv"
