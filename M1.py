"""(q3.py) M/M/c queueing system with monitor
   and multiple replications"""

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
    count = 0
    def run(self, mu):
        Arrival.count += 1
        Arrival.n += 1
        arrivetime = now()
        G.numbermon.observe(Arrival.n)

        if (Arrival.n > 0):
            G.busymon.observe(1)
        else:
            G.busymon.observe(0)

        # print Arrival.n,now(), "Event: Customer arrive and start service"
        yield request, self, G.server
        t = random.expovariate(1.0/mu)
        yield hold, self, t
        yield release, self, G.server

        delay = now() - arrivetime
        # print Arrival.n, delay, "Event: Customer leaves"
        G.delaymon.observe(delay)

        Arrival.n -= 1
        G.numbermon.observe(Arrival.n)

        if (Arrival.n > 0):
            G.busymon.observe(1)

        else:
            G.busymon.observe(0)

class G:
    server = 'dummy'
    delaymon = 'Monitor'
    numbermon = 'Monitor'
    busymon = 'Monitor'

def model(c, N, lamb, mu, maxtime, rvseed):
    # setup
    initialize()
    random.seed(rvseed)
    G.server = Resource(c, monitored=True)
    G.delaymon = Monitor()
    G.numbermon = Monitor()
    G.busymon = Monitor()

    # simulate
    s = Source('Source')
    activate(s, s.run(N, lamb, mu))
    simulate(until=maxtime)

    # gather performance measures
    W = G.delaymon.mean()
    L = G.numbermon.timeAverage()
    B = G.busymon.timeAverage()
    Lamb_eff = L/W
    Arrival.n = 0
    return (W,L,B,Lamb_eff)


## Experiment ----------

allW,allL = [],[]
allB,all_lamb_eff = [], []
for k in range(50):
    seed = 123 * k
    result = model(c=1, N=10000, lamb=1.612, mu=0.563898,
                   maxtime=2000000, rvseed=seed)
    allW.append(result[0])
    allL.append(result[1])
    allB.append(result[2])
    all_lamb_eff.append(result[3])


print ""
print "Estimate of W:", numpy.mean(allW)
print "Conf int of W:", conf(allW)
print "Estimate of L:", numpy.mean(allL)
print "Conf int of L:", conf(allL)
print "Estimate of B:", numpy.mean(allB)
print "Conf int of B:", conf(allB)
print "Estimate of lamb_eff:", numpy.mean(all_lamb_eff)
print "Conf int of lam_eff:", conf(all_lamb_eff)

