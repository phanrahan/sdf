from sdf import sphere, X, Y, Z
import sym

def tet1(f):
    return f.fold(X-Y).fold(X-Z).fold(Y-Z)

def tet2(f):
    return f.fold(X+Y).fold(X+Z).fold(Y+Z)

def tet(f):
    return tet2(tet1(f))

f = sphere(.1).translate((1,1,1))
f = tet1(f)
f.save('tet.stl', bounds=((-4, -4, -4), (4, 4, 4)))
