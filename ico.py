from math import sqrt, tan, pi
from np_sdf import abs, sign, min, cross, vec3, mat3, matmul
from sdf import sdf3, sphere, capsule, plane, rectangle
from ops import surface, groove
import sym

PHI = (1.+sqrt(5.))/2.
A = PHI / sqrt( 1. + PHI*PHI )
B = 1. / sqrt( 1. + PHI*PHI )

V1 = vec3(B,0,A)
V2 = vec3(A,B,0)
V3 = vec3(0,A,B)

def ico(fund):
    return fund.fold(cross(V1,V2)).fold(cross(V2,V3)).fold(cross(V3,V1)).fold()

R = 25
G = 2

e1 = surface(plane(cross(V1, V2)))
e2 = surface(plane(cross(V2, V3)))
e3 = surface(plane(cross(V3, V1)))
e = e1 | e3 | e2
g = rectangle(G).rotate(pi/4)
s = groove(sphere(R),e,g)

#s1 = sphere(0.1).translate(V1)
#s2 = sphere(0.1).translate(V2)
#s3 = sphere(0.1).translate(V3)
#s1 = capsule(V1, V2,0.1)
#s2 = capsule(V2, V3,0.1)
#s3 = capsule(V3, V1,0.1)
#s = s1 | s2 | s3

s = ico(s)

D = R+5
step = D/128
s.translate((step/2,step/2,step/2)).save('ico.stl', step=step, bounds=((-D, -D, -D), (D, D, D)))
