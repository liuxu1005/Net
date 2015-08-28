import random,sys,math
from optparse import OptionParser
from PS8_netsim import *
import PS8_tests

### Skeleton for distance vector routing lab in 6.02

# use our own node class derived from the node class of lab8_net.py
# so we can override routing behavior
class DVRouter(Router):
    INFINITY = 32

    def send_advertisement(self, time):
        adv = self.make_dv_advertisement()
        for link in self.links:
            p = self.network.make_packet(self.address, self.peer(link), 
                                         'ADVERT', time,
                                         color='red', ad=adv)
            link.send(self, p)        
            
    # Make a distance vector protocol advertisement, which will be sent
    # by the caller along all the links
    def make_dv_advertisement(self):
        ## Your code here
        adv = []
        for k in self.routes:
            adv.append((k, self.spcost[k]))
        return adv

    def link_failed(self, link):
        ## Your code here
        todel = [] 
        for k in self.routes:
            if self.routes[k] == link:
                self.spcost[k] = self.INFINITY
                self.routes[k] = None
        return

    def process_advertisement(self, p, link, time):
        self.integrate(link, p.properties['ad'])

    # Integrate new routing advertisement to update routing
    # table and costs
    def integrate(self,link,adv):
        ## Your code here
        tmproute = {}
        tmpspcost = {}
        for k in adv:
             if k[0] in self.routes:
                 if self.routes[k[0]] == link:
                     if k[1] + link.cost < self.INFINITY:
                         self.spcost[k[0]] = link.cost + k[1]
                     else:
                         self.routes[k[0]] = None
                         self.spcost[k[0]] = self.INFINITY
                 else:
                     if self.spcost[k[0]] > link.cost + k[1]:
                         self.routes[k[0]] = link
                         self.spcost[k[0]] = link.cost + k[1]
             else:
                 if k[1] + link.cost < self.INFINITY:
                     tmproute[k[0]] = link
                     tmpspcost[k[0]] = k[1] + link.cost
                 else:
                     tmproute[k[0]] = None
                     tmpspcost[k[0]] = self.INFINITY
             
        if len(tmpspcost) > 0:
            self.spcost.update(tmpspcost)
        if len(tmproute) > 0:
            self.routes.update(tmproute)
        return          

# A network with nodes of type DVRouter.
class DVRouterNetwork(RouterNetwork):
    # nodes should be an instance of DVNode (defined above)
    def make_node(self,loc,address=None):
        return DVRouter(loc,address=address)

########################################################################

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-g", "--gui", action="store_true", dest="gui", 
                      default=False, help="show GUI")
    parser.add_option("-n", "--numnodes", type="int", dest="numnodes", 
                      default=12, help="number of nodes")
    parser.add_option("-t", "--simtime", type="int", dest="simtime", 
                      default=2000, help="simulation time")
    parser.add_option("-r", "--rand", action="store_true", dest="rand", 
                      default=False, help="use randomly generated topology")
#    parser.add_option("-l", "--loss", type="float", dest="lossprob", 
#                      default=0.0, help="link packet loss probability")
#    parser.add_option("-f", "--mttf", type="int", dest="mttf", 
#                      default=10000, help="mean time between failures")
    
    (opt, args) = parser.parse_args()

    if opt.rand == True:
        rg = RandomGraph(opt.numnodes)
        (NODES, LINKS) = rg.genGraph()
    else:
        # build the deterministic test network
        #   A---B   C---D
        #   |   | / | / |
        #   E   F---G---H
        # format: (name of node, x coord, y coord)

        NODES =(('A',0,0), ('B',1,0), ('C',2,0), ('D',3,0),
                ('E',0,1), ('F',1,1), ('G',2,1), ('H',3,1))

        # format: (link start, link end)
        LINKS = (('A','B'),('A','E'),('B','F'),('E','F'),
                 ('C','D'),('C','F'),('C','G'),
                 ('D','G'),('D','H'),('F','G'),('G','H'))

    # setup graphical simulation interface
    if opt.gui == True:
        net = DVRouterNetwork(opt.simtime, NODES, LINKS, 0)
        sim = NetSim()
        sim.SetNetwork(net)
        sim.MainLoop()
    else:
        PS8_tests.verify_routes(DVRouterNetwork)
