from sdf import sphere, X, Y, Z
import sym

TET1VERT    = (-1,-1,-1)
TET1MIDEDGE = (0,0,-1)
TET1MIDFACE = (-1,1,-1)

def tet1(f):
    return f.fold(X-Y).fold(X-Z).fold(Y-Z)


TET2VERT    = (1,1,1)
TET2MIDEDGE = (0,0,1)
TET2MIDFACE = (-1,1,1)

def tet2(f):
    return f.fold(X+Y).fold(X+Z).fold(Y+Z)


def tet(f):
    return tet2(tet1(f))

f = sphere(.1).translate(TET2VERT)
f |= sphere(.1).translate(TET2MIDEDGE)
f |= sphere(.1).translate(TET2MIDFACE)
f = tet1(f)

D = 2
f.save('tet.stl', step=D/128, bounds=((-D, -D, -D), (D, D, D)))
