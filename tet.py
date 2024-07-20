from math import pi
from np_sdf import cross
from sdf import sphere, plane, rectangle
from ops import surface, groove
from sym import subdivide

V1 = ( 1,-1, 1)
V2 = ( 1, 1,-1)
V3 = (-1, 1, 1)

def tet(f):
    return f.fold(cross(V1,V2)).fold(cross(V2,V3)).fold(cross(V3,V1))

if __name__ == '__main__':
    R = 25
    G = 2

    s = subdivide(sphere(R), G, V1, V2, V3, 0)

    s = tet(s)

    D = R+5
    step = D/128
    s.translate((step/2,step/2,step/2)).save('tet.stl', step=step, bounds=((-D, -D, -D), (D, D, D)))
