from math import pi
from np_sdf import cross
from sdf import sphere, plane, rectangle
from ops import surface, groove
import sym

V1 = ( 1,-1, 1)
V2 = ( 1, 1,-1)
V3 = (-1, 1, 1)

def tet(f):
    return f.fold(cross(V1,V2)).fold(cross(V2,V3)).fold(cross(V3,V1))

if __name__ == '__main__':
    R = 25
    G = 2

    e1 = surface(plane(cross(V1, V2)))
    e2 = surface(plane(cross(V2, V3)))
    e3 = surface(plane(cross(V3, V1)))
    e = e1 | e3 | e2
    g = rectangle(G).rotate(pi/4)
    s = groove(sphere(R),e,g)

    s = tet(s)

    D = R+5
    step = D/128
    s.translate((step/2,step/2,step/2)).save('tet.stl', step=step, bounds=((-D, -D, -D), (D, D, D)))
