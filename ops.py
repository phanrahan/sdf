# from http://mercury.sexy/hg_sdf/
# explained in more detail at https://www.ronja-tutorials.com/

from math import sqrt
from glsl import np, abs, min, max, vec, vec3, vec2d, vec3d, length, tan, atan2, cos, sin, arcsinh
from sdf import sdf2, sdf3, op3, union, intersection, plane, circle, rectangle, X, Y, Z, ORIGIN, UP

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

# loxodrome or rhumb line - constant bearing
#   https://en.wikipedia.org/wiki/Rhumb_line
@op3
def rhumb(other, beta):
    tanbeta = 1/tan(beta)
    def f(p):
        x = p[:,0]
        y = p[:,1]
        z = p[:,2]
        phi = atan2(z,length(vec(x,y)))
        theta = tanbeta * arcsinh(tan(phi))
        c = cos(-theta)
        s = sin(-theta)
        x2 = c * x - s * y
        y2 = s * x + c * y
        z2 = z
        return other(vec(x2, y2, z2))
    return f

# shell(other, 0)
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

def union_round(a, b, r):
    u = a | b
    c = rectangle(r).translate((r/2,r/2))-circle(r).translate((r,r))
    f = sweep(a, b, c)
    return u | f

def intersection_round(a, b, r):
    i = a & b
    c = rectangle(r).translate((-r/2,-r/2))-circle(r).translate((-r,-r))
    f = sweep(a, b, c)
    return i - f

def difference_round(a, b, r):
    return intersection_round(a, negate(b), r)

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

# https://www.shadertoy.com/view/3lBfRK

@sdf2
def polygon(points):
    points = [np.array(p) for p in points]
    def f(p):
        n = len(points)
        d = dot(p - points[0], p - points[0])
        s = np.ones(len(p))
        for i in range(n):
            j = (i + n - 1) % n
            vi = points[i]
            vj = points[j]
            if np.array_equal(vi, vj):
                continue
            e = vj - vi
            w = p - vi
            b = w - e * np.clip(np.dot(w, e) / np.dot(e, e), 0, 1).reshape((-1, 1))
            d = min(d, dot(b, b))
            c1 = p[:,1] >= vi[1]
            c2 = p[:,1] < vj[1]
            c3 = e[0] * w[:,1] > e[1] * w[:,0]
            c = vec(c1, c2, c3)
            s = np.where(np.all(c, axis=1) | np.all(~c, axis=1), -s, s)
        return s * np.sqrt(d)
    return f
