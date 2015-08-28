#demodulate workfile: 6.02 PS 4,5,6
import numpy
import sendrecv
import math

def avgfilter(samples_in, window):
    #raise NotImplementedError, "avgfilter"
        rlt = []
        size = 0
        leng = len(samples_in)
        for i in range(leng):
            if (i + window) > leng:
                size = leng - i
            else:
                size = window
            
            rlt.append( float(sum(samples_in[i: i + size]))/size)
        return numpy.array(rlt)
    

def lpfilter(samples_in, omega_cut):
    raise NotImplementedError, "lpfilter"

def envelope_demodulator(samples, sample_rate, carrier_freq, spb):
    #raise NotImplementedError, "envelope_demodulator"
    abs_sample = [abs(i) for i in samples]
    return avgfilter(abs_sample, (sample_rate/carrier_freq)/2)

def heterodyne_demodulator(samples, sample_rate, carrier_freq, spb):
    raise NotImplementedError, "hetero_demodulator"

def avg_demodulator(samples, sample_rate, carrier_freq, spb):
    raise NotImplementedError, "avg_demodulator"

def quad_demodulator(samples, sample_rate, carrier_freq, spb, channel_gap = 500):
    raise NotImplementedError, "quad_demodulator"
