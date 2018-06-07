import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


def poisson(k, mean: int=1):
    """
    Poisson distribution
    :param k: integer value(s)
    :param mean: mean of the distribution
    :return: probability of the specified value(s)
    """
    fact = np.vectorize(np.math.factorial)
    return mean ** k * np.e ** (-mean) / fact(k)


def bus_prob(counts):
    bus1_probability = poisson(counts, 1)
    bus7_probability = poisson(counts, 7)
    bus8_probability = poisson(counts, 8)

    plt.plot(counts, bus1_probability, color='r', label='bus1')
    plt.plot(counts, bus7_probability, color='g', label='bus7')
    plt.plot(counts, bus8_probability, color='b', label='any bus')
    plt.xlabel('n - bus count per hour')
    plt.ylabel('P(n)')
    plt.title('Poisson distribution of bus count per hour')
    plt.legend()
    plt.savefig("plots/bus_probabilities.png")
    plt.show()




if __name__ == '__main__':
    bus_count = np.arange(0, 20)
    # bus_prob(bus_count)

    bus_count = np.arange(0, 10)
    time = np.arange(0, 5)
    probs_1 = []
    probs_7 = []
    for t in time:
        probs_1.append(poisson(bus_count, 1 * t)[0])
        probs_7.append(poisson(bus_count, 7 * t))

    probs_1 = np.array(probs_1)  # t
    probs_7 = np.array(probs_7)  # t x m
    probs_joint_per_time = probs_7.T * probs_1
    probs_joint = np.sum(probs_joint_per_time, axis=1)

    p2 = np.zeros((len(time), len(bus_count)))
    fact = np.vectorize(np.math.factorial)
    for t in time:
        p2[t,:] = (7 * t) ** bus_count * np.e ** (-8*t) / fact(bus_count)
    p2_ = np.sum(p2, axis=0)

    print(np.sum(p2_))
    # TODO 1 - normalization?, 2 wrong joint prob
    plt.plot(bus_count, probs_joint, color='r')
    plt.plot(bus_count, p2_, color='b')
    plt.xlabel('m - count of bus7 arrived before bus1')
    plt.ylabel('P(m)')
    plt.title('Poisson distribution of bus count')
    plt.savefig("plots/bus7_before1.png")
    plt.show()

