import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
import load_data_script as load
import math

""" data analysis with chi-square goodness of fit"""


def obs_cts(n, data):
    """ given: the data and number of bins
        returns: the observed values and the bin edges as lists"""
    events, edges = np.histogram(data, n)
    return events.tolist(), edges.tolist()


def exp_cts(n, data,rv):
    """ given: the data and number of bins
        returns: the expected values and prob over each of the bins with
        the necessary modification of the first and last bins"""
    L = []
    P_bins = []
    for x in obs_cts(n, data)[1]:
        L.append(rv.cdf(x))
    P_bins.append(L[1])
    for i in range(1, len(L) - 2):
        P_bins.append(L[i + 1] - L[i])
    P_bins.append(1 - L[-2])
    exp_cnt = [x * len(data) for x in P_bins]
    return exp_cnt, P_bins


def ind_bins_to_reduce(f_exp):
    """ given: a list
        returns: the indexes of the elements < 5"""
    NC_to_red = [index for index, value in enumerate(f_exp) if value < 5]
    return NC_to_red


def one_reduce(f_exp, f_obs, f_edge):
    """ given: lists of exp, obs, edges
        returns: new lists with one reduced bin with value < 5 """
    BTR = ind_bins_to_reduce(f_exp)

    if (len(BTR) > 1 or (len(BTR) == 1 and BTR[0] != 0)):
        f_exp[BTR[-1] - 1] = f_exp[BTR[-1] - 1] + f_exp[BTR[-1]]
        f_obs[BTR[-1] - 1] = f_obs[BTR[-1] - 1] + f_obs[BTR[-1]]
        del (f_edge[BTR[-1]])
        del (f_obs[BTR[-1]])
        del (f_exp[BTR[-1]])
    else:
        if BTR[0] == 0:
            f_exp[1] = f_exp[1] + f_exp[0]
            f_obs[1] = f_obs[1] + f_obs[0]
            del (f_edge[1])
            del (f_obs[0])
            del (f_exp[0])

    f_expN = f_exp
    f_obsN = f_obs
    f_edgeN = f_edge
    BTRN = ind_bins_to_reduce(f_expN)
    return f_expN, f_obsN, f_edgeN, BTRN


def all_reduce(f_expF, f_obsF, f_edgeF, BTRF):
    """ finalizes the bin reduction """
    while BTRF != []:
        u = one_reduce(f_expF, f_obsF, f_edgeF)
        f_expF = u[0]
        f_obsF = u[1]
        f_edgeF = u[2]
        BTRF = u[3]
    return f_expF, f_obsF, f_edgeF, BTRF


def model(data, n, dof, rv):
    """ given data, the number of bins (n) and the number of estimated parameters (dof)
    produces the value of the chi-squate test statistics and the p-value"""

    ## final expected count and final observed count after amalgamating bins

    exp, obs = all_reduce(exp_cts(n, data,rv)[0], obs_cts(n, data)[0],
                          obs_cts(n, data)[1], ind_bins_to_reduce(exp_cts(n, data,rv)[0]))[0:2]

    # build in chi-gof test, the last argument is the adjustment to the dof
    result = ss.chisquare(np.asarray(obs), np.asarray(exp), dof)
    return result

def count_bin(test_set):
    size = len(test_set)
    bin = int(1 + math.log(size,2))
    return bin

def draw_hist(input_list,n_bins,rv,title,color):

    # create the histogram of the data for n bins
    myHist = plt.hist(input_list, n_bins, normed=True, color=color)

    # plot the density of this gamma rv
    x = np.linspace(0.001, 500)
    h = plt.plot(x, rv.pdf(x), lw=2)
    plt.title(title)
    name = title +'.png'
    plt.savefig(name)
    plt.show()


def test_gamma_dist(input_list,list_name):
    # parameter estimation (in ss.gamma EX=alpha*beta, V(X)= alpha*beta*beta)!!!!
    fit_alpha, fit_loc, fit_beta = ss.gamma.fit(input_list, floc=0)

    rv = ss.gamma(fit_alpha, fit_loc, fit_beta)
    print 'fit alpha is %.4f and fit beta is %.4f' % (fit_alpha,fit_beta)

    # chose the number of bins
    n = count_bin(input_list)
    print 'number of bins %i' % n

    name = 'test Gamma on ' + list_name
    draw_hist(input_list,n,rv,name,'crimson')

    # set the adjustment to dof (degree of freedom) = to the number of parameters estimated
    dof = 2

    ##  experiment--------------------------------------------------
    result = model(input_list, n, dof,rv)
    t_value,p_value = result[0],result[1]
    print "The chi_sq test value of gamma dist is %5.6f and the p-value is %5.6f" %(t_value,p_value)


def test_expoential_dist(input_list,list_name):
    # parameter estimation (in ss.gamma EX=alpha*beta, V(X)= alpha*beta*beta)!!!!
    fit_loc,fit_lamb = ss.expon.fit(input_list,floc=0)

    rv = ss.expon( fit_loc,fit_lamb)
    print 'fit lambda is %.4f ' % (fit_lamb)

    # chose the number of bins
    n = count_bin(input_list)
    print 'number of bins %i' % n

    name = 'test Exponential on ' + list_name
    draw_hist(input_list, n, rv, name, 'burlywood')

    # set the adjustment to dof (degree of freedom) = to the number of parameters estimated
    dof = 2

    ##  experiment--------------------------------------------------
    result = model(input_list, n, dof, rv)
    t_value, p_value = result[0], result[1]
    print "The chi_sq test value of exponential dist is %5.6f and the p-value is %5.6f" % (t_value, p_value)


def test_erlang_dist(input_list,list_name):
    # erlang is a special dist of gamma with int shape alpha
    fit_alpha, fit_loc, fit_beta = ss.erlang.fit(input_list,floc=0)

    rv = ss.erlang(int(fit_alpha), fit_loc, fit_beta)
    print 'fit alpha is %.4f and fit beta is %.4f' %(int(fit_alpha), fit_beta)

    # chose the number of bins
    n = count_bin(input_list)
    print 'number of bins %i' % n

    name = 'test Erlang on ' + list_name
    draw_hist(input_list, n, rv, name, 'Chartreuse')

    # set the adjustment to dof (degree of freedom) = to the number of parameters estimated
    dof = 1

    ##  experiment--------------------------------------------------
    result = model(input_list, n, dof, rv)
    t_value, p_value = result[0], result[1]
    print "The chi_sq test value of erlang dist is %5.6f and the p-value is %5.10f" % (t_value, p_value)


if __name__ == "__main__":
    ## experiment data --------------------------------------------------------------
    data_dir = '/home/tian/PycharmProjects/312-Group/Final data.txt'
    print data_dir
    int_arr, service_time = load.make_total_sets(data_dir)

    test_set = [int_arr,service_time]

    print '\n-------------------------------------------------------'
    print 'test on interval arrival time set'
    name = 'int arr t'
    test_expoential_dist(int_arr, name)
    test_gamma_dist(int_arr, name)
    test_erlang_dist(int_arr, name)

    print '\n-------------------------------------------------------'
    print 'test on service time set'
    name = 'service t'
    test_expoential_dist(service_time, name)
    test_gamma_dist(service_time, name)
    test_erlang_dist(service_time, name)




