import load_data_script as load
import numpy as np
import scipy
import math
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

def count_bin(test_set):
    size = len(test_set)
    bin = int(1 + math.log(size,2))
    return bin

def draw_graph(data,color,title):
    ys = scipy.rand(10000)
    xs = [draw_empirical(data, a) for a in ys]
    plt.scatter(xs, ys,s=0.1,alpha=0.5)
    plt.hist(data,bins=count_bin(data),normed=1,histtype='step',cumulative=True,color=color)
    plt.title(title)
    name = title + '.png'
    plt.savefig(name)
    plt.show()


if __name__ == "__main__":
    ## experiment data --------------------------------------------------------------
    data_dir = '/home/tian/PycharmProjects/312-Group/Final data.txt'

    int_arr, service_time = load.make_total_sets(data_dir)

    test_set = [int_arr,service_time]
    draw_graph(int_arr,color='crimson',title='intarrival time')
    draw_graph(service_time,color='burlywood',title='service time')

