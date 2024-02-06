from math import pi
from np_sdf import cross
from sdf import sphere, plane, rectangle
from ops import surface, groove
from sym import subdivide

V1 = (1,0,0)
V2 = (0,1,0)
V3 = (0,0,1)

def oct(f):
    return f.fold()

if __name__ == '__main__':
    R = 25
    G = 2

    s = subdivide(sphere(R), G, V1, V2, V3)

    s = oct(s)

    D = R+5
    step = D/128
    s.translate((step/2,step/2,step/2)).save('oct.stl', step=step, bounds=((-D, -D, -D), (D, D, D)))
