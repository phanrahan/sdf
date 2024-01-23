from math import sqrt
import numpy as np
from sdf import *
from quadrics import double_cone

_min = np.minimum
_max = np.maximum
_abs = np.abs

def _length(a):
    return np.linalg.norm(a, axis=1)

def _vec(*arrs):
    return np.stack(arrs, axis=-1)

# first object gets a v-shaped engraving where it intersect the second
@op3
def engrave(a, b, r):
    def f(p):
        d1 = a(p)
        d2 = b(p)
        return _max(d1, (d1 + r - abs(d2))*sqrt(0.5))
    return f

@op3
def union_chamfer(a, b, r):
    def f(p):
        d1 = a(p)
        d2 = b(p)
        return _min(_min(d1, d2), (d1 - r + d2)*sqrt(0.5))
    return f

@op3
def union_round(a, b, r):
    def f(p):
        d1 = a(p)
        d2 = b(p)
        u = _max(_vec(r - d1,r - d2), np.array((0,0)))
        return _max(r, _min (d1, d2)) - _length(u)
    return f

