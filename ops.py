# from http://mercury.sexy/hg_sdf/
# explained in more detail at https://www.ronja-tutorials.com/

from math import sqrt
from np_sdf import np, abs, min, max, length
from sdf import sdf3, op3, plane, X, Y, Z, ORIGIN, UP

def gradient(f, p):
    h = 0.0001 # replace by an appropriate value
    k0 = vec3((1,-1,-1))
    k1 = vec3((-1,-1,1))
    k2 = vec3((-1,1,-1)) 
    k3 = vec3((1,1,1))
    return _normalize( k0*f( p + k0*h ) 
                     + k1*f( p + k1*h )
                     + k2*f( p + k2*h )
                     + k3*f( p + k3*h ) )

@sdf3
def fan(n):
    return plane(Y).surface().circular_array(n)

@sdf3
def slices(d):
    return plane(Z).surface().repeat((0,0,d))


@op3
def surface(other):
    def f(p):
        return abs(other(p))
    return f

# first object gets a v-shaped engraving where it intersect the second
@op3
def vgroove(a, b, r):
    def f(p):
        d1 = a(p)
        d2 = b(p)
        # groove extends r into a, center of the groove is along b
        return max(d1, (d1 + r - abs(d2))*sqrt(0.5))
    return f

# first object gets a v-shaped engraving where it intersect the second
@op3
def vemboss(a, b, r):
    def f(p):
        d1 = a(p)
        d2 = b(p)
        # emboss extends r out of a, center of the groove is along b
        return min(d1, (d1 - r + abs(d2))*sqrt(0.5))
    return f

# first object gets a circula-shaped engraving where it intersect the second
@op3
def cgroove(a, b, r):
    def f(p):
        d1 = a(p)
        d2 = b(p)
        # form pipe of radius r at intersection
        d = length(vec(d1,d2)) - r
        # difference(a, d) 
        return max(d1, -d)
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

# https://www.ronja-tutorials.com/post/035-2d-sdf-combination/#champfer
# https://www.blakecourter.com/2022/06/25/edge-coordinate-system.html
# https://www.blakecourter.com/2022/06/22/constant-width-chamfer.html
# sum (S) is the clearance
# difference (D) is the mid-surface
# two-body = D/S
#
# also intersection_chamfer, difference_chamfer
@op3
def union_chamfer(a, b, r):
    def f(p):
        d1 = a(p)
        d2 = b(p)
        # union( union(a,b), dilate(S(a,b), r))
        return min(min(d1, d2), (d1 + d2 - r)*sqrt(0.5))
    return f

# At right-angle intersections between objects,
# build a new local coordinate system from the two distances 
# to combine them in interesting ways.
@op3
def union_round(a, b, r):
    def f(p):
        d1 = a(p)
        d2 = b(p)
        u = max(vec(r - d1,r - d2), vec3((0,0)))
        return max(r, min (d1, d2)) - length(u)
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
        return other( vec(x(p), y(p), z(p)) );
