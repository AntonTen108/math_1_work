"""
Численное интегрирование функции f(x) = x^2 / (25 - x^2) на отрезке [1, 4]

Точное значение: -3 + (5/2) * ln(6) ≈ 1.47940007...

Методы:
  1. Метод средних прямоугольников
  2. Метод трапеций
  3. Метод Симпсона

Для каждого метода:
  - вычисление при n in {10, 50, 100, 500, 1000}
  - абсолютная и относительная погрешность
  - визуализация аппроксимирующих фигур при n = 10
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# ─────────────────────────────────────────────
#  Параметры задачи
# ─────────────────────────────────────────────
a, b = 1.0, 4.0
NS = [10, 50, 100, 500, 1000]
EXACT = -3 + 2.5 * math.log(6)          # аналитическое значение


def f(x):
    return x ** 2 / (25 - x ** 2)


# ─────────────────────────────────────────────
#  Численные методы
# ─────────────────────────────────────────────
def midpoint_rect(n: int) -> float:
    """Метод средних прямоугольников."""
    h = (b - a) / n
    return h * sum(f(a + h * (i + 0.5)) for i in range(n))


def trapezoid(n: int) -> float:
    """Метод трапеций."""
    h = (b - a) / n
    s = f(a) + f(b)
    s += 2 * sum(f(a + h * i) for i in range(1, n))
    return s * h / 2


def simpson(n: int) -> float:
    """Метод Симпсона (n должно быть чётным)."""
    if n % 2 != 0:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 != 0 else 2) * f(a + h * i)
    return s * h / 3


# ─────────────────────────────────────────────
#  Погрешности
# ─────────────────────────────────────────────
def abs_error(approx: float) -> float:
    return abs(approx - EXACT)


def rel_error(approx: float) -> float:
    return abs_error(approx) / abs(EXACT) * 100


# ─────────────────────────────────────────────
#  Таблицы результатов
# ─────────────────────────────────────────────
def print_table(method_name: str, method_fn):
    print(f"\n{'='*70}")
    print(f"  {method_name}")
    print(f"{'='*70}")
    print(f"  Точное значение: {EXACT:.10f}")
    print(f"{'─'*70}")
    print(f"  {'n':>6}  {'Значение':>16}  {'|Δ| абс.':>16}  {'δ% отн.':>14}")
    print(f"{'─'*70}")
    for n in NS:
        v = method_fn(n)
        ae = abs_error(v)
        re = rel_error(v)
        print(f"  {n:>6}  {v:>16.10f}  {ae:>16.2e}  {re:>13.8f}%")
    print(f"{'─'*70}")


# ─────────────────────────────────────────────
#  Визуализация — прямоугольники
# ─────────────────────────────────────────────
def plot_midpoint(ax, n=10):
    h = (b - a) / n
    x_fine = np.linspace(a, b, 600)
    ax.plot(x_fine, f(x_fine), color='#378ADD', linewidth=2.5, label='f(x)', zorder=5)

    for i in range(n):
        x0, x1 = a + h * i, a + h * (i + 1)
        xm = (x0 + x1) / 2
        ym = f(xm)
        rect = plt.Rectangle((x0, 0), h, ym,
                              facecolor='#1D9E7533', edgecolor='#1D9E75',
                              linewidth=1.2, zorder=3)
        ax.add_patch(rect)
        ax.plot(xm, ym, 'o', color='#1D9E75', ms=4, zorder=6)

    ax.set_title(f'Метод средних прямоугольников  (n = {n})', fontsize=13, pad=10)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_xlim(0.7, 4.3)
    ax.set_ylim(-0.05, 2.1)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)
    val = midpoint_rect(n)
    ax.text(0.98, 0.04, f'I ≈ {val:.6f}', transform=ax.transAxes,
            ha='right', fontsize=10, color='#1D9E75')


# ─────────────────────────────────────────────
#  Визуализация — трапеции
# ─────────────────────────────────────────────
def plot_trapezoid(ax, n=10):
    h = (b - a) / n
    x_fine = np.linspace(a, b, 600)
    ax.plot(x_fine, f(x_fine), color='#378ADD', linewidth=2.5, label='f(x)', zorder=5)

    nodes_x = [a + h * i for i in range(n + 1)]
    nodes_y = [f(x) for x in nodes_x]

    for i in range(n):
        xs = [nodes_x[i], nodes_x[i+1], nodes_x[i+1], nodes_x[i]]
        ys = [0, 0, nodes_y[i+1], nodes_y[i]]
        poly = Polygon(list(zip(xs, ys)),
                       facecolor='#BA751733', edgecolor='#BA7517',
                       linewidth=1.2, zorder=3)
        ax.add_patch(poly)

    ax.plot(nodes_x, nodes_y, 'o-', color='#BA7517', ms=5,
            linewidth=1.2, zorder=6, label='Узлы трапеций')

    ax.set_title(f'Метод трапеций  (n = {n})', fontsize=13, pad=10)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_xlim(0.7, 4.3)
    ax.set_ylim(-0.05, 2.1)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)
    val = trapezoid(n)
    ax.text(0.98, 0.04, f'I ≈ {val:.6f}', transform=ax.transAxes,
            ha='right', fontsize=10, color='#BA7517')


# ─────────────────────────────────────────────
#  Визуализация — Симпсон
# ─────────────────────────────────────────────
def plot_simpson(ax, n=10):
    if n % 2 != 0:
        n += 1
    h = (b - a) / n
    x_fine = np.linspace(a, b, 600)
    ax.plot(x_fine, f(x_fine), color='#378ADD', linewidth=2.5, label='f(x)', zorder=5)

    for i in range(0, n, 2):
        x0, x1, x2 = a + h * i, a + h * (i + 1), a + h * (i + 2)
        y0, y1, y2 = f(x0), f(x1), f(x2)

        # коэффициенты параболы через три точки
        d = h
        A = (y0 - 2*y1 + y2) / (2 * d**2)
        B = (y2 - y0) / (2 * d)
        C = y1

        # точки параболы
        t = np.linspace(x0, x2, 60)
        dx = t - x1
        y_par = A * dx**2 + B * dx + C

        # заливка
        ax.fill_between(t, 0, y_par,
                        facecolor='#534AB733', edgecolor='none', zorder=3)
        # контур
        ax.plot(t, y_par, color='#534AB7', linewidth=1.8, zorder=4)

        # узлы
        ax.plot([x0, x1, x2], [y0, y1, y2], 'o',
                color='#534AB7', ms=5, zorder=6)

    ax.set_title(f'Метод Симпсона  (n = {n})', fontsize=13, pad=10)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_xlim(0.7, 4.3)
    ax.set_ylim(-0.05, 2.1)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)
    val = simpson(n)
    ax.text(0.98, 0.04, f'I ≈ {val:.6f}', transform=ax.transAxes,
            ha='right', fontsize=10, color='#534AB7')


# ─────────────────────────────────────────────
#  График сходимости
# ─────────────────────────────────────────────
def plot_convergence(ax):
    ae_rect = [abs_error(midpoint_rect(n)) for n in NS]
    ae_trap = [abs_error(trapezoid(n))     for n in NS]
    ae_simp = [abs_error(simpson(n))       for n in NS]

    ax.semilogy(NS, ae_rect, 'o-',  color='#1D9E75', label='Прямоугольники', linewidth=2)
    ax.semilogy(NS, ae_trap, 's--', color='#BA7517', label='Трапеции',       linewidth=2)
    ax.semilogy(NS, ae_simp, '^:',  color='#534AB7', label='Симпсон',        linewidth=2)

    ax.set_title('Сходимость методов (абс. погрешность)', fontsize=13, pad=10)
    ax.set_xlabel('n (число узлов)')
    ax.set_ylabel('|Δ| (лог. шкала)')
    ax.set_xticks(NS)
    ax.legend(fontsize=10)
    ax.grid(True, which='both', alpha=0.3)


# ─────────────────────────────────────────────
#  Главная функция
# ─────────────────────────────────────────────
def main():
    print("\n" + "="*70)
    print("  ЧИСЛЕННОЕ ИНТЕГРИРОВАНИЕ  f(x) = x² / (25 − x²)  на [1, 4]")
    print("="*70)
    print(f"\n  Точное значение: EXACT = −3 + (5/2)·ln(6) = {EXACT:.10f}")

    print_table("Метод средних прямоугольников", midpoint_rect)
    print_table("Метод трапеций",                trapezoid)
    print_table("Метод Симпсона",                simpson)

    # ── Итоговое сравнение ──────────────────────────────────────
    print(f"\n{'='*70}")
    print("  ИТОГОВОЕ СРАВНЕНИЕ при n = 1000")
    print(f"{'─'*70}")
    for name, fn in [("Прямоугольники", midpoint_rect),
                     ("Трапеции",       trapezoid),
                     ("Симпсон",        simpson)]:
        v = fn(1000)
        print(f"  {name:<20} I = {v:.10f}   |Δ| = {abs_error(v):.2e}   "
              f"δ = {rel_error(v):.2e}%")
    print(f"{'='*70}\n")

    # ── Графики ─────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Численное интегрирование  $f(x)=x^2/(25-x^2)$  на $[1,\\,4]$',
                 fontsize=14, fontweight='bold', y=0.98)
    fig.patch.set_facecolor('#F8F8F6')
    for ax in axes.flat:
        ax.set_facecolor('#FAFAF8')

    plot_midpoint(axes[0, 0])
    plot_trapezoid(axes[0, 1])
    plot_simpson(axes[1, 0])
    plot_convergence(axes[1, 1])

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('numerical_integration.png', dpi=150, bbox_inches='tight')
    print("  Графики сохранены в numerical_integration.png")
    plt.show()


if __name__ == '__main__':
    main()