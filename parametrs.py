import math

a, b = 1.0, 4.0
NS = [10, 50, 100, 500, 1000]
EXACT = -3 + 2.5 * math.log(6)

def f(x):
    return x ** 2 / (25 - x ** 2)


