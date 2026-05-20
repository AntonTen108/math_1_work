def plot_midpoint(ax, n=10):
    x_fine = np.linspace(A, B, 600)
    ax.plot(x_fine, f(x_fine), color='#2563EB', lw=2.5, label='f(x)', zorder=5)

    h = (B - A) / n
    for i in range(n):
        x0 = A + h * i
        xm = x0 + h / 2
        ym = f(xm)
        rect = patches.Rectangle((x0, 0), h, ym,
                                 linewidth=1.2, edgecolor='#059669',
                                 facecolor='#D1FAE5', alpha=0.85, zorder=3)
        ax.add_patch(rect)
        ax.plot(xm, ym, 'o', color='#059669', ms=4, zorder=6)

    ax.axhline(0, color='#aaa', lw=0.8)
    ax.set_xlim(0.7, 4.4)
    ax.set_ylim(-0.1, 2.3)
    ax.set_title(f'Метод средних прямоугольников (n = {n})', fontsize=13, fontweight='bold', pad=10)
    ax.set_xlabel('x');
    ax.set_ylabel('f(x)')
    val = midpoint_rect(f, A, B, n)
    ae = abs_error(val, EXACT)
    ax.legend(loc='upper left', fontsize=10)
    ax.text(0.98, 0.04, f'I ≈ {val:.6f}\n|Δ| = {ae:.2e}',
            transform=ax.transAxes, ha='right', va='bottom',
            fontsize=9, color='#059669',
            bbox=dict(boxstyle='round,pad=0.4', fc='#F0FDF4', ec='#059669', alpha=0.85))
    ax.grid(True, alpha=0.25, lw=0.7)