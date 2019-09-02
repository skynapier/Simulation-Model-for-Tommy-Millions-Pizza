
from SimPy.Simulation import *
import random
import numpy
import math


## Useful extras ----------
def conf(L):
    """confidence interval"""
    lower = numpy.mean(L) - 1.96 * numpy.std(L) / math.sqrt(len(L))
    upper = numpy.mean(L) + 1.96 * numpy.std(L) / math.sqrt(len(L))
    return (lower, upper)


## Model ----------
class Source(Process):
    """generate random arrivals"""

    def run(self, N, lamb, mu):
        for i in range(N):
            a = Arrival(str(i))
            activate(a, a.run(mu))
            t = random.expovariate(1.0/lamb)
            yield hold, self, t


class Arrival(Process):
    """an arrival"""
    n = 0
    def run(self, mu):

        Arrival.n += 1
        arrivetime = now()
        G.numbermon.observe(Arrival.n)

        if (Arrival.n > 0):
            G.busymon.observe(1)
        else:
            G.busymon.observe(0)

        # print Arrival.n, now(), "Event: Customer arrive and start service"
        yield request, self, G.server
        # alpha = 3.0112   beta = 0.1873
        t = random.gammavariate(3.0,0.1873)
        G.servicemon.observe(t)
        G.servicesquaredmon.observe(t ** 2)
        yield hold, self, t
        yield release, self, G.server

        Arrival.n -= 1
        G.numbermon.observe(Arrival.n)

        if (Arrival.n > 0):
            G.busymon.observe(1)
        else:
            G.busymon.observe(0)

        delay = now() - arrivetime
        G.delaymon.observe(delay)

class G:
    server = 'dummy'
    delaymon = 'Monitor'
    numbermon = 'Monitor'
    busymon = 'Monitor'
    servicemon = 'Monitor'
    servicesquaredmon = 'Monitor'

def model(c, N, lamb, mu, maxtime, rvseed):
    # setup
    initialize()
    random.seed(rvseed)
    G.server = Resource(c, monitored=True)
    G.delaymon = Monitor()
    G.numbermon = Monitor()
    G.busymon = Monitor()
    G.servicemon = Monitor()
    G.servicesquaredmon = Monitor()

    # simulate
    s = Source('Source')
    activate(s, s.run(N, lamb, mu))
    simulate(until=maxtime)

    # gather performance measures
    W = G.delaymon.mean()
    L = G.numbermon.timeAverage()
    B = G.busymon.timeAverage()
    S = G.servicemon.mean()
    S2 = G.servicesquaredmon.mean()
    LQ = G.server.waitMon.timeAverage()
    Lamb_eff = L / W
    wQ = LQ / Lamb_eff

    Y = wQ - Lamb_eff * S2 / (2.0 * (1 - B))


    Arrival.n = 0
    return (W,L,B,Lamb_eff,Y,S)


## Experiment ----------

allW,allL,allY = [],[],[]
allB,all_lamb_eff = [], []
allS = []
for k in range(50):
    seed = 123 * k
    result = model(c=1, N=10000, lamb=1.612, mu=0.563898,
                   maxtime=2000000, rvseed=seed)
    allW.append(result[0])
    allL.append(result[1])
    allB.append(result[2])
    all_lamb_eff.append(result[3])
    allY.append(result[4])
    allS.append(result[5])

print ""
print "Estimate of W:", numpy.mean(allW)
print "Conf int of W:", conf(allW)
print "Estimate of L:", numpy.mean(allL)
print "Conf int of L:", conf(allL)
print "Estimate of B:", numpy.mean(allB)
print "Conf int of B:", conf(allB)
print "Estimate of lamb_eff:", numpy.mean(all_lamb_eff)
print "Conf int of lam_eff:", conf(all_lamb_eff)
print "Estimate of Y:", numpy.mean(allY)
print "Conf int of Y:", conf(allY)
print "Estimate of S:", numpy.mean(allS)
print "Conf int of S:", conf(allS)

