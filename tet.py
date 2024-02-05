from math import sqrt, pi
import numpy as np
from np_sdf import cross
from sdf import sphere, plane, rectangle, X, Y, Z
from ops import surface, groove
import sym

def dot(u,v):
    return np.sum(u*v)

def foldp(p, n):
    p = np.array(p)
    n = n/sqrt(dot(n,n))
    d = min(dot(p,n), 0)
    p = p - 2. * d * n
    return p

TET1VERT    = (1,1,1)
TET1MIDEDGE = (0,0,-1)
TET1MIDFACE = (-1,1,1)

def tet1(f):
    return f.fold(X-Y).fold(X-Z).fold(Y-Z)


TET2VERT    = (-1,-1,-1)
TET2MIDEDGE = (0,0,1)
TET2MIDFACE = (-1,1,1)

V1 = ( 1,-1, 1)
V2 = ( 1, 1,-1)
V3 = (-1, 1, 1)

def tet2(f):
    return f.fold(X+Y).fold(X+Z).fold(Y+Z)


def tet(f):
    return tet2(tet1(f))

#print(foldp(foldp(foldp(TET2VERT,Y+Z),X+Z),X+Y))
#print(foldp(foldp(foldp((-1,-1, 1),Y+Z),X+Z),X+Y))
#print(foldp(foldp(foldp((-1, 1,-1),Y+Z),X+Z),X+Y))
#print(foldp(foldp(foldp(( 1,-1,-1),Y+Z),X+Z),X+Y))

#print(foldp(foldp(foldp(TET2MIDEDGE,Y+Z),X+Z),X+Y))
#print(foldp(foldp(foldp((1,0,0),Y+Z),X+Z),X+Y))

#print(foldp(foldp(foldp(TET2MIDFACE,Y+Z),X+Z),X+Y))
#print(foldp(foldp(foldp((1,-1,1),Y+Z),X+Z),X+Y))



R = 25
G = 2

e1 = surface(plane(cross(V1, V2)))
e2 = surface(plane(cross(V2, V3)))
e3 = surface(plane(cross(V3, V1)))
e = e1 | e3 | e2
g = rectangle(G).rotate(pi/4)
s = groove(sphere(R),e,g)

#s = sphere(.1).translate(TET1VERT)
#s |= sphere(.1).translate(TET2MIDEDGE)
#s |= sphere(.1).translate(TET2MIDFACE)

s = tet2(s)

D = R+5
step = D/128
s.translate((step/2,step/2,step/2)).save('tet.stl', step=step, bounds=((-D, -D, -D), (D, D, D)))
