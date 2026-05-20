def abs_error(approx, exact):
    """Абсолютная погрешность."""
    return abs(approx - exact)


def rel_error(approx, exact):
    """Относительная погрешность в процентах."""
    return abs(approx - exact) / abs(exact) * 100
