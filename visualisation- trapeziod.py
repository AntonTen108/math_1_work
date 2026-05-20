def plot_trapezoidal(ax, n=10):
    x_fine = np.linspace(A, B, 600)
    ax.plot(x_fine, f(x_fine), color='#2563EB', lw=2.5, label='f(x)', zorder=5)

    h = (B - A) / n
    xs = np.linspace(A, B, n + 1)
    ys = f(xs)

    for i in range(n):
        verts = [(xs[i], 0), (xs[i], ys[i]), (xs[i + 1], ys[i + 1]), (xs[i + 1], 0)]
        poly = Polygon(verts, closed=True,
                       facecolor='#FEF3C7', edgecolor='#D97706',
                       linewidth=1.2, alpha=0.85, zorder=3)
        ax.add_patch(poly)

    ax.plot(xs, ys, 'o-', color='#D97706', ms=5, lw=1.2, zorder=6, label='узлы')
    ax.axhline(0, color='#aaa', lw=0.8)
    ax.set_xlim(0.7, 4.4)
    ax.set_ylim(-0.1, 2.3)
    ax.set_title(f'Метод трапеций (n = {n})', fontsize=13, fontweight='bold', pad=10)
    ax.set_xlabel('x');
    ax.set_ylabel('f(x)')
    val = trapezoidal(f, A, B, n)
    ae = abs_error(val, EXACT)
    ax.legend(loc='upper left', fontsize=10)
    ax.text(0.98, 0.04, f'I ≈ {val:.6f}\n|Δ| = {ae:.2e}',
            transform=ax.transAxes, ha='right', va='bottom',
            fontsize=9, color='#D97706',
            bbox=dict(boxstyle='round,pad=0.4', fc='#FFFBEB', ec='#D97706', alpha=0.85))
    ax.grid(True, alpha=0.25, lw=0.7)