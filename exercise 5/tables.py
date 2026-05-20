from config import NS, f_area, f_length
from methods import simpson
from errors import abs_error, rel_error
from exact import EXACT_S, EXACT_L


def print_tables():
    print("\n" + "=" * 72)
    print("  r(φ) = 3 / (1 + 0.8·cos φ),   φ ∈ [0, 2π]")
    print("=" * 72)
    print(f"  Эталон (scipy.quad):  S = {EXACT_S:.10f}   L = {EXACT_L:.10f}")

    for label, func, exact in [
        ("ПЛОЩАДЬ  S", f_area, EXACT_S),
        ("ДЛИНА ДУГИ  L", f_length, EXACT_L),
    ]:
        print(f"\n{'─' * 72}")
        print(f"  {label}  (метод Симпсона)")
        print(f"{'─' * 72}")
        print(f"  {'n':>6}  {'Значение':>18}  {'|Δ| абс.':>14}  {'δ% отн.':>14}")
        print(f"{'─' * 72}")
        for n in NS:
            v = simpson(func, n)
            ae = abs_error(v, exact)
            re = rel_error(v, exact)
            print(f"  {n:>6}  {v:>18.10f}  {ae:>14.2e}  {re:>13.8f}%")
        print(f"{'─' * 72}")
