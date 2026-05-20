import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Wedge
from config import alpha, beta, r, f_area, f_length
from methods import simpson
from exact import EXACT_S, EXACT_L
from errors import abs_error


def plot_polar_curve(ax):
    phi = np.linspace(alpha, beta, 1000)
    rho = r(phi)
    ax.plot(phi, rho, color='#378ADD', linewidth=2.2, label=r'$r(\varphi)=\frac{3}{1+0.8\cos\varphi}$')
    ax.fill(phi, rho, alpha=0.12, color='#378ADD')
    ax.set_title('Кривая в полярных координатах', fontsize=12, pad=12)
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(True, alpha=0.3)


def plot_sectors(ax, n=20):
    phi_nodes = np.linspace(alpha, beta, n + 1)
    h = (beta - alpha) / n

    for i in range(n):
        phi_m = (phi_nodes[i] + phi_nodes[i + 1]) / 2
        r_m = r(phi_m)
        deg0 = np.degrees(phi_nodes[i])
        deg1 = np.degrees(phi_nodes[i + 1])
        color = plt.cm.viridis(i / n)
        wedge = Wedge(
            center=(0, 0),
            r=r_m,
            theta1=deg0,
            theta2=deg1,
            facecolor=color,
            alpha=0.35,
            edgecolor='white',
            linewidth=0.5,
            transform=ax.transData._b
        )

    phi_fine = np.linspace(alpha, beta, 800)
    rho_fine = r(phi_fine)
    x_fine = rho_fine * np.cos(phi_fine)
    y_fine = rho_fine * np.sin(phi_fine)
    ax.plot(x_fine, y_fine, color='#378ADD', linewidth=2.2,
            label=r'$r(\varphi)$')

    for i in range(n):
        phi_m = (phi_nodes[i] + phi_nodes[i + 1]) / 2
        r_m = r(phi_m)
        color = plt.cm.viridis(i / n)

        phi_arc = np.linspace(phi_nodes[i], phi_nodes[i + 1], 30)
        x_arc = r_m * np.cos(phi_arc)
        y_arc = r_m * np.sin(phi_arc)

        x_sec = np.concatenate([[0], x_arc, [0]])
        y_sec = np.concatenate([[0], y_arc, [0]])
        ax.fill(x_sec, y_sec, color=color, alpha=0.35,
                edgecolor='white', linewidth=0.4)

    ax.set_aspect('equal')
    ax.set_title(f'Аппроксимация площади круговыми секторами (n = {n})',
                 fontsize=11, pad=10)
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(True, alpha=0.25)


def plot_errors(ax_s, ax_l):
    ns_range = np.arange(10, 501, 10)
    ae_s = [abs_error(simpson(f_area, n), EXACT_S) for n in ns_range]
    ae_l = [abs_error(simpson(f_length, n), EXACT_L) for n in ns_range]

    ax_s.semilogy(ns_range, ae_s, color='#1D9E75', linewidth=2)
    ax_s.set_title('Сходимость: площадь S', fontsize=11, pad=8)
    ax_s.set_xlabel('n')
    ax_s.set_ylabel('|Δ| (лог. шкала)')
    ax_s.grid(True, which='both', alpha=0.3)

    ax_l.semilogy(ns_range, ae_l, color='#534AB7', linewidth=2)
    ax_l.set_title('Сходимость: длина дуги L', fontsize=11, pad=8)
    ax_l.set_xlabel('n')
    ax_l.set_ylabel('|Δ| (лог. шкала)')
    ax_l.grid(True, which='both', alpha=0.3)


def draw_all(save_path='polar_integration.png'):
    fig = plt.figure(figsize=(15, 10))
    fig.suptitle(
        r'Полярная кривая  $r(\varphi)=\dfrac{3}{1+0.8\cos\varphi}$,  '
        r'$\varphi\in[0,\,2\pi]$',
        fontsize=14, fontweight='bold', y=0.98
    )
    fig.patch.set_facecolor('#F8F8F6')

    ax_polar = fig.add_subplot(2, 2, 1, projection='polar')
    ax_cart = fig.add_subplot(2, 2, 2)
    ax_err_s = fig.add_subplot(2, 2, 3)
    ax_err_l = fig.add_subplot(2, 2, 4)

    for ax in [ax_cart, ax_err_s, ax_err_l]:
        ax.set_facecolor('#FAFAF8')

    plot_polar_curve(ax_polar)
    plot_sectors(ax_cart, n=20)
    plot_errors(ax_err_s, ax_err_l)

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    print(f"\n  Графики сохранены в {save_path}")
    plt.show()

