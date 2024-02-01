from sdf import sphere, X, Y, Z
import sym

def cube(f):
    return f.fold()

def oct1(f):
    return f.fold(X+Y).fold(X-Y).fold(Y+Z).fold(Y-Z)
    #return f.fold(X+Y).fold(Y+Z).fold(Z)

# ( ±1, 0, 0 );
# ( 0, ±1, 0 );
# ( 0, 0, ±1 ).
def oct(f):
    return f.fold().fold(X-Y).fold(X-Z).fold(Y-Z)

#f = sphere(0.1).translate((1,1,1))
f = sphere(0.1).translate((1,0,0))
f = oct1(f)

D = 2
f.save('oct.stl', step=D/128, bounds=((-D, -D, -D), (D, D, D)))
