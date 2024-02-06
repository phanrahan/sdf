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

def subdivide(s, G, V1, V2, V3):
    e1 = surface(plane(cross(V1, V2)))
    e2 = surface(plane(cross(V2, V3)))
    e3 = surface(plane(cross(V3, V1)))
    e = e1 | e3 | e2
    g = rectangle(G).rotate(pi/4)
    return groove(s,e,g)

