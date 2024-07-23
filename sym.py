from math import pi
from np_sdf import np, abs, min, vec3, dot, cross, normalize
from ops import surface, groove
from sdf import op3, plane, rectangle

def unit_plane(n):
    return plane(normalize(n))

@op3
def fold(other, n=None):
    if n is not None:
        #isinstance(my_array, np.ndarray)
        n = normalize(n)
    def f(p):
        if n is None:
            p = abs(p)
        else:
            d = min(dot(p, n), 0)
            p -= 2 * np.outer(d, n)
        return other(p)
    return f

def triangle(V1,V2,V3):
    e1 = surface(unit_plane(cross(V1, V2)))
    e2 = surface(unit_plane(cross(V2, V3)))
    e3 = surface(unit_plane(cross(V3, V1)))
    return e1 | e2 | e3

def subdivide(V1, V2, V3, n):
    V1 = normalize(V1)
    V2 = normalize(V2)
    V3 = normalize(V3)
    if n > 0:
        V12 = V1 + V2
        V23 = V2 + V3
        V31 = V3 + V1
        s = subdivide(V12,V23,V31,n-1)
        s = s.fold(cross(V12,V23)).fold(cross(V23,V31)).fold(cross(V31,V12))
    else:
        s = triangle(V1,V2,V3)
    return s


#def ico(fund):
#    return fund.fold(cross(V1,V2)).fold(cross(V2,V3)).fold(cross(V3,V1)).fold()

#def oct(f):
#    return f.fold()

#def tet(f):
#    return f.fold(cross(V1,V2)).fold(cross(V2,V3)).fold(cross(V3,V1))
