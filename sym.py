from math import pi
from np_sdf import np, abs, min, vec3, dot, cross, normalize
from ops import surface, groove
from sdf import op3, plane, rectangle

@op3
def fold(other, n=None):
    if n is not None:
        n = normalize(vec3(n))
    def f(p):
        if n is None:
            p = abs(p)
        else:
            d = min(dot(p, n), 0)
            p -= 2 * np.outer(d, n)
        return other(p)
    return f

def triangle(s,V1,V2,V3,G):
    e1 = surface(plane(cross(V1, V2)))
    e2 = surface(plane(cross(V2, V3)))
    e3 = surface(plane(cross(V3, V1)))
    e = e1 | e2 | e3
    g = rectangle(G).rotate(pi/4)
    return groove(s,e,g)

def subdivide(s, V1, V2, V3, G, n):
    #V1 = normalize(V1)
    #V2 = normalize(V2)
    #V3 = normalize(V3)
    if n > 0:
        V12 = V1 + V2
        V23 = V2 + V3
        V31 = V3 + V1
        s = subdivide(s,V12,V23,V31,n-1)
        s = s.fold(cross(V12,V23)).fold(cross(V23,V31)).fold(cross(V31,V12))
        #s = subdivide(s,V23,V31,V12,n-1)
        #s = s.fold(cross(V23,V12)).fold(cross(V31,V23)).fold(cross(V12,V31))
    else:
        s = triangle(s,V1,V2,V3,G)
    return s




