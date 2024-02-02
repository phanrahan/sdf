# from http://mercury.sexy/hg_sdf/
# explained in more detail at https://www.ronja-tutorials.com/

from math import sqrt
from np_sdf import np, abs, min, max, vec, vec3, vec2d, vec3d, length
from sdf import sdf3, op3, union, plane, circle, rectangle, X, Y, Z, ORIGIN, UP

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

@op3
def place(a, b, c, shape):
    def f(p):
        return shape( vec3d(a(p), b(p), c(p)) )
    return f

@op3
def sweep(a, b, shape):
    def f(p):
        return shape( vec2d(a(p), b(p)) )
    return f

def pipe(a, b, r=1):
    return sweep(a, b, circle(r))

# first object gets a v-shaped engraving where it intersect the second
def groove(a, b, c):
    return a - sweep(a, b, c)

# first object gets a v-shaped engraving where it intersect the second
def emboss(a, b, c):
    return a | sweep(a, b, c)

def fillet(a, b, r):
    return union(a.dilate(r), b.dilate(r)).erode(r)

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
