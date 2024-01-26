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
        # groove extends r into a, center of the groove is along b
        return _max(d1, (d1 + r - _abs(d2))*sqrt(0.5))
    return f

# first object gets a v-shaped engraving where it intersect the second
@op3
def vemboss(a, b, r):
    def f(p):
        d1 = a(p)
        d2 = b(p)
        # emboss extends r out of a, center of the groove is along b
        return _min(d1, (d1 - r + _abs(d2))*sqrt(0.5))
    return f

# first object gets a circula-shaped engraving where it intersect the second
@op3
def cgroove(a, b, r):
    def f(p):
        d1 = a(p)
        d2 = b(p)
        # form pipe of radius r at intersection
        d = _length(_vec(d1,d2)) - r
        # difference(a, d) 
        return _max(d1, -d)
    return f

#// first object gets a capenter-style groove cut out
#float fOpGroove(float a, float b, float ra, float rb) {
#   intersect(a, union(erode(a, ra), negate(dilate(abs(b), rb))... 
#	return max(a, min(a + ra, rb - abs(b)));
#}

#// first object gets a capenter-style tongue attached
#float fOpTongue(float a, float b, float ra, float rb) {
#   union(a, intersection(delate(a, ra), dilate(abs(b), rb))... 
	#return min(a, max(a - ra, abs(b) - rb));
#}

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
def displace( other, displacment ):
    def f(p):
        d1 = other(p);
        d2 = displacement(p);
        return d1+d2;
    return f

@op3
def deform( other, x, y, z ):
    def f(p):
        return other( _vec(x(p), y(p), z(p)) );
