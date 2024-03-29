from math import sqrt, pi
from np_sdf import vec3, cross 
from sdf import sphere, plane, rectangle
from ops import surface, groove
from sym import triangle, subdivide

PHI = (1.+sqrt(5.))/2.
A = PHI / sqrt( 1. + PHI*PHI )
B = 1. / sqrt( 1. + PHI*PHI )

V1 = vec3(B,0,A)
V2 = vec3(A,B,0)
V3 = vec3(0,A,B)

def ico(fund):
    return fund.fold(cross(V1,V2)).fold(cross(V2,V3)).fold(cross(V3,V1)).fold()

if __name__ == '__main__':
    #s = triangle(sphere(25),V1,V2,V3, G=1)
    s = sphere(25)
    s =  ico(subdivide(s, V1, V2, V3, 1))

    D = 30
    step = D/128
    s.translate((step/2,step/2,step/2)).save('ico.stl', step=step, bounds=((-D, -D, -D), (D, D, D)))
