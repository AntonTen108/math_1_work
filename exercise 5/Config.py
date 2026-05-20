import numpy as np

alpha = 0.0
beta = 2 * np.pi
NS = [200, 500, 1000]


def r(phi):
    return 3 / (1 + 0.8 * np.cos(phi))


def dr(phi):
    return (3 * 0.8 * np.sin(phi)) / (1 + 0.8 * np.cos(phi)) ** 2


def f_area(phi):
    return 0.5 * r(phi) ** 2


def f_length(phi):
    return np.sqrt(r(phi) ** 2 + dr(phi) ** 2)
