import sys
from math import pi
from sdf import plane, slab, sphere, rectangle, X, Y, Z
from quadrics import double_cone
from ops import fan, slices, groove

R = 25.
SHELL = .15*R
SMOOTH = 1.
G = 0.25
N = 24

GROVE = rectangle(G).rotate(pi/4)


def diamond(s):
    f = fan(N)
    diag1 = f.twist( pi).scale(R)
    diag2 = f.twist(-pi).scale(R)
    s = groove(s, diag1.orient(X), GROVE)
    s = groove(s, diag2.orient(X), GROVE)
    return s

def triangle(s):
    s = diamond(s)
    s = groove(s, fan(2*N).orient(X), GROVE)
    return s

# not working ...
def hex(s):
    f = fan(N)
    diag1 = f.twist( pi/2).scale(R)
    diag2 = f.twist(-pi/2).scale(R)
    s = groove(s, diag1.orient(X), GROVE)
    s = groove(s, diag2.orient(X), GROVE)
    s = groove(s, f.orient(X), GROVE)
    #s = groove(s, fan(N).rotate(pi/(2*N), Z).orient(X), GROVE)
    return s


def baseball(s):
    # subtract an inner sphere to form shell
    s = s - sphere(R-SHELL)

    # remove a double cone oriented in Z, smooth the intersection
    f = s - double_cone().k(SMOOTH)
    # remove positive x halfspace
    f &= slab(x0=-2*R, x1=0)

    # form a double cone shaped cap oriented along Y
    g = s & (double_cone().orient(Y).k(SMOOTH))

    # return the union of the two pieces
    return f | g

s = sphere(R) 

name = "ball"
if len(sys.argv) > 1:
    name = sys.argv[1]
    if name == 'diamond':
        s = diamond(s)
    elif name == 'triangle':
        s = triangle(s)
    elif name == 'hex':
        s = hex(s)
    else:
        print("usage: python ornament.py [diamond|triangle|hex]")
        sys.exit(0)

ornament = baseball(s)

ornament = ornament.translate((0.05,0.05,0.05))
ornament.save(name+'.stl', step=(0.1, 0.1, 0.1), bounds=((-30,-30,-30),(30,30,30)))
