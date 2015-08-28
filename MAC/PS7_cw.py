# 6.02 PSet: CSMA with windowed stabilization

import random, sys, wx, math, time
from optparse import OptionParser
from PS7_wsim import *
import matplotlib.pyplot as p

###############################################################

class WinCSMANode(WirelessNode):
    def __init__(self,location,network,retry):
        WirelessNode.__init__(self,location,network,retry)
        ## Your code to initialize any additional state or variables goes here
        ## You can use self.network.cwmin, self.network.cwmax, etc.
        ## See the WinCSMAWirelessNetwork class defined below
        self.cw = self.network.cwmax
        self.st = 0 #random.randint(1, self.network.stats.simtime)
        # for plots of collisions/success
        self.sent = []
        self.coll = []
        
    def channel_access(self,time,ptime,numnodes):
        # You can tell if the channel is busy or not using
        # the self.network.channel_busy() function call.
        ## Your code here
        if self.network.channel_idle() and self.st > 0:
            self.st = self.st - 1
        if len(self.transmit_queue) > 0 and\
           self.st == 0 and\
           self.network.channel_idle():
            return True
        else:
            return False

    def on_collision(self,packet):
        # for plots of collisions
        self.coll.append(self.network.time)

        ## Your code here
        if self.cw * 2 > self.network.cwmax:
            self.cw = self.network.cwmax
        else:
            self.cw = self.cw * 2
        self.st = random.randint(1, self.cw)
        return
    def on_xmit_success(self,packet):
        # for plots of successful transmissions
        self.sent.append(self.network.time)

        ## Your code here
        if self.cw / 2 < self.network.cwmin:
            self.cw = self.network.cwmin
        else:
            self.cw = self.cw / 2
        self.st = random.randint(1, self.cw)
        return
################################################################

class WinCSMAWirelessNetwork(WirelessNetwork):
    def __init__(self,n,chantype,ptime,dist,load,retry,backoff,
		 skew,qmax,cwmin,cwmax,simtime):
        self.cwmin = cwmin
        self.cwmax = cwmax      
        WirelessNetwork.__init__(self,n,chantype,ptime,dist,load,retry,backoff,
                                 skew,qmax,simtime)

    def make_node(self,loc,retry):
        return WinCSMANode(loc,self,retry)

################################################################

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-g", "--gui", action="store_true", dest="gui", 
                      default=False, help="show GUI")
    parser.add_option("-n", "--numnodes", type="int", dest="numnodes", 
                      default=16, help="number of nodes")
    parser.add_option("-t", "--simtime", type="int", dest="simtime", 
                      default=10000, help="simulation time")
    parser.add_option("-b", "--backoff", dest="backoff", 
                      default='Mine', help="backoff scheme (Mine, None)")
    parser.add_option("-s", "--size", type="int", dest="ptime", 
                      default=1, help="packet size (in time units)")
    parser.add_option("-w", "--cwmin", type="int", dest="cwmin", 
                      default=1, help="min contention window size")    
    parser.add_option("-W", "--cwmax", type="int", dest="cwmax", 
                      default=256, help="max contention window size")    
    parser.add_option("-l", "--load", type="int", dest="load", 
                      default=100, help="total load % (in pkts/timeslot)")
    parser.add_option("-r", "--retry", action="store_true", dest="retry", 
                      default=False, help="show GUI")
    parser.add_option("-k", "--skew", action="store_true", dest="skew", 
                      default=False, help="skew source loads")

    (opt, args) = parser.parse_args()
    print 'Protocol: Windowed CSMA with stabilization'

    wnet = WinCSMAWirelessNetwork(opt.numnodes,'WinCSMA',opt.ptime,
                               'exponential',opt.load,opt.retry,opt.backoff,
                               opt.skew,0,opt.cwmin,opt.cwmax,opt.simtime)

    if opt.gui == True:
        sim = NetSim()
        sim.SetNetwork(wnet)
        sim.MainLoop()
    else:
        wnet.step(opt.simtime)
        plot_data(wnet)         # in PS8_wsim
