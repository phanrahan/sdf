# from http://mercury.sexy/hg_sdf/

from math import sqrt
import numpy as np
from sdf import sdf3, op3, X, Y, Z, ORIGIN, UP
from quadrics import double_cone

_min = np.minimum
_max = np.maximum
_abs = np.abs
_dot = np.dot

def _normalize(a):
    return a / np.linalg.norm(a)

def _length(a):
    return np.linalg.norm(a, axis=1)

def _vec(*arrs):
    return np.stack(arrs, axis=-1)

@sdf3
def flatplane(normal=UP, point=ORIGIN):
    normal = _normalize(normal)
    def f(p):
        return _abs(_dot(point - p, normal))
    return f

# first object gets a v-shaped engraving where it intersect the second
@op3
def vgroove(a, b, r):
    def f(p):
        d1 = a(p)
        d2 = b(p)
        return _max(d1, (d1 + r - _abs(d2))*sqrt(0.5))
    return f

# first object gets a v-shaped engraving where it intersect the second
@op3
def vemboss(a, b, r):
    def f(p):
        d1 = a(p)
        d2 = b(p)
        return _min(d1, (d1 - r + _abs(d2))*sqrt(0.5))
    return f

# first object gets a circula-shaped engraving where it intersect the second
@op3
def cgroove(a, b, r):
    def f(p):
        d1 = a(p)
        d2 = b(p)
        d = _length(_vec(d1,d2)) - r
        return _max(d1, -d)
    return f

@op3
def union_chamfer(a, b, r):
    def f(p):
        d1 = a(p)
        d2 = b(p)
        return _min(_min(d1, d2), (d1 - r + d2)*sqrt(0.5))
    return f

# At right-angle intersections between objects,
# build a new local coordinate system from the two distances 
# to combine them in interesting ways.
@op3
def union_round(a, b, r):
    def f(p):
        d1 = a(p)
        d2 = b(p)
        u = _max(_vec(r - d1,r - d2), np.array((0,0)))
        return _max(r, _min (d1, d2)) - _length(u)
    return f

