""" draw from an empirical distribution, uses the inverse
    transformation method and linear interpolation"""

import numpy as np
import random
import scipy
import pylab
import matplotlib.pyplot as plt


def draw_empirical(data, r):
    """one draw (for given r ~ U(0,1)) from the
    empirical cdf based on data"""

    d = {x: data.count(x) for x in data}
    obs_values, freq = zip(*sorted(zip(d.keys(), d.values())))
    obs_values = list(obs_values)
    freq = list(freq)
    empf = [x * 1.0 / len(data) for x in freq]
    ecum = np.cumsum(empf).tolist()
    ecum.insert(0, 0)
    obs_values.insert(0, 0)

    for x in ecum:
        if r <= x:
            rpt = x
            break
    r_end = ecum.index(rpt)
    y = obs_values[r_end] - 1.0 * (ecum[r_end] - r) * (obs_values[r_end] -
                                                       obs_values[r_end - 1]) / (ecum[r_end] - ecum[r_end - 1])
    return y


# Experiment ---------
data = [3.8, 7.5, 8.0, 1.9, 4.5, 6.6, 7.1, 7.5, 2.8, 4.5]
r = 0.8

print r
print draw_empirical(data, r)

ys = scipy.rand(10000)
xs = [draw_empirical(data, a) for a in ys]
myHist = plt.hist(data, 10, normed=True)
plt.scatter(xs,ys)
plt.show()
# pylab.scatter(xs,ys)
# pylab.show()