def print_table(method_func, method_name, exact):
    print(f"\n{'═' * 72}")
    print(f"  {method_name}")
    print(f"{'═' * 72}")
    print(f"  {'n':>6}  {'Значение':>16}  {'|Δ| абс.':>16}  {'δ% отн.':>14}")
    print(f"  {'-' * 6}  {'-' * 16}  {'-' * 16}  {'-' * 14}")
    for n in NS:
        val = method_func(f, A, B, n)
        ae = abs_error(val, exact)
        re = rel_error(val, exact)
        print(f"  {n:>6}  {val:>16.10f}  {ae:>16.2e}  {re:>13.8f}%")
    print(f"{'═' * 72}")


def print_all_tables():
    print(f"\n  Точное значение интеграла: {EXACT:.10f}")
    print(f"  (= -3 + (5/2) * ln(6))\n")
    print_table(midpoint_rect, "МЕТОД СРЕДНИХ ПРЯМОУГОЛЬНИКОВ", EXACT)
    print_table(trapezoidal, "МЕТОД ТРАПЕЦИЙ", EXACT)
    print_table(simpson, "МЕТОД СИМПСОНА", EXACT)