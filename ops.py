# from http://mercury.sexy/hg_sdf/

from math import sqrt
import numpy as np
from sdf import *
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

# form a curve of radius r at the intersection of the two surfaces
@op3
def pipe(a, b, r):
    def f(p):
        d1 = a(p)
        d2 = b(p)
        print("d1 = ", d1.shape())
        print("d2 = ", d2.shape())
        return _length(_vec(d1,d2)) - r
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


@op3
def circular_array(other, count, offset=0):
    other = other.translate(X * offset)
    da = np.pi / count
    def f(p):
        x = p[:,0]
        y = p[:,1]
        z = p[:,2]
        d = np.hypot(x, y)
        a = np.arctan2(y, x) % da
        d1 = other(_vec(np.cos(a - da) * d, np.sin(a - da) * d, z))
        d2 = other(_vec(np.cos(a) * d, np.sin(a) * d, z))
        return _min(d1, d2)
    return f
