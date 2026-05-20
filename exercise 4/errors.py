def abs_error(approx, exact):

    return abs(approx - exact)


def rel_error(approx, exact):

    return abs(approx - exact) / abs(exact) * 100
