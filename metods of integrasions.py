
import numpy as np
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
def midpoint_rect(func, a, b, n):
    """Метод средних прямоугольников."""
    h = (b - a) / n
    return h * sum(func(a + h * (i + 0.5)) for i in range(n))


def trapezoidal(func, a, b, n):
    """Метод трапеций."""
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)
    return h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])


def simpson(func, a, b, n):
    """Метод Симпсона (составная формула). n должно быть чётным."""
    if n % 2 != 0:
        n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)
    return h / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
