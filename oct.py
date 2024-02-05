from math import sqrt, pi
from np_sdf import cross
from sdf import sphere, plane, rectangle, X, Y, Z
from ops import surface, groove
import sym

# ( ±1, 0, 0 );
# ( 0, ±1, 0 );
# ( 0, 0, ±1 ).
def oct(f):
    return f.fold()

V1 = (1,0,0)
V2 = (0,1,0)
V3 = (0,0,1)

#f = sphere(0.1).translate((1,1,1))
#f = sphere(0.1).translate((1,0,0))
#f = oct1(f)

R = 25
G = 2

e1 = surface(plane(cross(V1, V2)))
e2 = surface(plane(cross(V2, V3)))
e3 = surface(plane(cross(V3, V1)))
e = e1 | e3 | e2
g = rectangle(G).rotate(pi/4)
s = groove(sphere(R),e,g)

s = oct(s)

D = R+5
step = D/128
s.translate((step/2,step/2,step/2)).save('oct.stl', step=step, bounds=((-D, -D, -D), (D, D, D)))
