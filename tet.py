from math import sqrt
import numpy as np
from sdf import sphere, X, Y, Z
import sym

def dot(u,v):
    return np.sum(u*v)

def foldp(p, n):
    p = np.array(p)
    n = n/sqrt(dot(n,n))
    d = min(dot(p,n), 0)
    p = p - 2. * d * n
    return p

TET1VERT    = (-1,-1,-1)
TET1MIDEDGE = (0,0,-1)
TET1MIDFACE = (-1,1,1)

def tet1(f):
    return f.fold(X-Y).fold(X-Z).fold(Y-Z)


TET2VERT    = (1,1,1)
TET2MIDEDGE = (0,0,1)
TET2MIDFACE = (-1,1,1)

def tet2(f):
    return f.fold(X+Y).fold(X+Z).fold(Y+Z)


def tet(f):
    return tet2(tet1(f))

print(foldp(foldp(foldp(TET2VERT,Y+Z),X+Z),X+Y))
print(foldp(foldp(foldp((-1,-1, 1),Y+Z),X+Z),X+Y))
print(foldp(foldp(foldp((-1, 1,-1),Y+Z),X+Z),X+Y))
print(foldp(foldp(foldp(( 1,-1,-1),Y+Z),X+Z),X+Y))

print(foldp(foldp(foldp(TET2MIDEDGE,Y+Z),X+Z),X+Y))
print(foldp(foldp(foldp((1,0,0),Y+Z),X+Z),X+Y))

print(foldp(foldp(foldp(TET2MIDFACE,Y+Z),X+Z),X+Y))
print(foldp(foldp(foldp((1,-1,1),Y+Z),X+Z),X+Y))


f = sphere(.1).translate(TET2VERT)
#f |= sphere(.1).translate(TET2MIDEDGE)
#f |= sphere(.1).translate(TET2MIDFACE)
f = tet2(f)

D = 2
#f.save('tet.stl', step=D/128, bounds=((-D, -D, -D), (D, D, D)))
