import numpy as np
from sdf import op3

_min = np.minimum

def _dot(a, b):
    return np.sum(a * b, axis=1)

@op3
def fold(other, n=None):
    if n is not None:
        n = np.array(n)
        n = n / np.linalg.norm(n)
    def f(p):
        if n is None:
            p = np.abs(p)
        else:
            d = _min(_dot(p, n), 0)
            p -= 2 * np.outer(d, n)
        return other(p)
    return f

#m = np.array([
#    [1-2*x*x,  -2*x*y,  -2*x*z],
#    [ -2*x*y, 1-2*y*y,  -2*y*z],
#    [ -2*x*z,  -2*y*z, 1-2*z*z],
#    ]).T
#p = np.dot(p, m)
