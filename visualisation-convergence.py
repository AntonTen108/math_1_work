import numpy as np
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

def plot_convergence(ax):
    ae_rect = [abs_error(midpoint_rect(f, A, B, n), EXACT) for n in NS]
    ae_trap = [abs_error(trapezoidal(f, A, B, n), EXACT) for n in NS]
    ae_simp = [abs_error(simpson(f, A, B, n), EXACT) for n in NS]

    ax.loglog(NS, ae_rect, 'o-', color='#059669', lw=2, ms=7, label='Прямоугольники')
    ax.loglog(NS, ae_trap, 's--', color='#D97706', lw=2, ms=7, label='Трапеции')
    ax.loglog(NS, ae_simp, '^:', color='#7C3AED', lw=2, ms=7, label='Симпсон')

    ax.set_xlabel('Число узлов n', fontsize=11)
    ax.set_ylabel('Абсолютная погрешность |Δ|', fontsize=11)
    ax.set_title('Сходимость методов', fontsize=13, fontweight='bold', pad=10)
    ax.legend(fontsize=10)
    ax.grid(True, which='both', alpha=0.3, lw=0.7)