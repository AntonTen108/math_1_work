import numpy as np
from Config import alpha, beta


def simpson(func, n):
    if n % 2 != 0:
        n += 1
    h = (beta - alpha) / n
    phi = np.linspace(alpha, beta, n + 1)
    y = func(phi)
    s = y[0] + y[-1]
    s += 4 * np.sum(y[1:-1:2])
    s += 2 * np.sum(y[2:-2:2])
    return s * h / 3
