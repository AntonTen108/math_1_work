import numpy as np
from scipy import integrate
from Config import f_area, f_length, alpha, beta

EXACT_S, _ = integrate.quad(f_area, alpha, beta)
EXACT_L, _ = integrate.quad(f_length, alpha, beta)
