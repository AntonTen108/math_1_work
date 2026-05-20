def plot_simpson(ax, n=10):
    if n % 2 != 0:
        n += 1
    x_fine = np.linspace(A, B, 600)
    ax.plot(x_fine, f(x_fine), color='#2563EB', lw=2.5, label='f(x)', zorder=5)

    h = (B - A) / n

    for i in range(0, n, 2):
        x0 = A + h * i
        x1 = x0 + h
        x2 = x0 + 2 * h
        y0, y1, y2 = f(x0), f(x1), f(x2)

        # коэффициенты параболы через три точки
        denom = (x0 - x1) * (x0 - x2)
        a_c = y0 / denom if denom != 0 else 0
        denom = (x1 - x0) * (x1 - x2)
        b_c = y1 / denom if denom != 0 else 0
        denom = (x2 - x0) * (x2 - x1)
        c_c = y2 / denom if denom != 0 else 0

        xp = np.linspace(x0, x2, 80)
        yp = (a_c * (xp - x1) * (xp - x2) +
              b_c * (xp - x0) * (xp - x2) +
              c_c * (xp - x0) * (xp - x1))

        verts_x = np.concatenate([[x0], xp, [x2]])
        verts_y = np.concatenate([[0], yp, [0]])
        verts = list(zip(verts_x, verts_y))
        poly = Polygon(verts, closed=True,
                       facecolor='#EDE9FE', edgecolor='#7C3AED',
                       linewidth=1.4, alpha=0.85, zorder=3)
        ax.add_patch(poly)

    xs = np.linspace(A, B, n + 1)
    ax.plot(xs, f(xs), 'o', color='#7C3AED', ms=4, zorder=6, label='узлы')
    ax.axhline(0, color='#aaa', lw=0.8)
    ax.set_xlim(0.7, 4.4)
    ax.set_ylim(-0.1, 2.3)
    ax.set_title(f'Метод Симпсона (n = {n})', fontsize=13, fontweight='bold', pad=10)
    ax.set_xlabel('x');
    ax.set_ylabel('f(x)')
    val = simpson(f, A, B, n)
    ae = abs_error(val, EXACT)
    ax.legend(loc='upper left', fontsize=10)
    ax.text(0.98, 0.04, f'I ≈ {val:.6f}\n|Δ| = {ae:.2e}',
            transform=ax.transAxes, ha='right', va='bottom',
            fontsize=9, color='#7C3AED',
            bbox=dict(boxstyle='round,pad=0.4', fc='#F5F3FF', ec='#7C3AED', alpha=0.85))
    ax.grid(True, alpha=0.25, lw=0.7)
