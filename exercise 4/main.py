def main():
    # ── Таблицы в консоль ──
    print_all_tables()

    # ── Графики ──
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Численное интегрирование  f(x) = x² / (25 − x²)  на [1, 4]',
                 fontsize=15, fontweight='bold', y=1.01)

    plot_midpoint(axes[0, 0], n=10)
    plot_trapezoidal(axes[0, 1], n=10)
    plot_simpson(axes[1, 0], n=10)
    plot_convergence(axes[1, 1])

    plt.tight_layout()
    plt.savefig('numerical_integration.png', dpi=150, bbox_inches='tight')
    print('\n  График сохранён в файл: numerical_integration.png')
    plt.show()


if __name__ == '__main__':
    main()