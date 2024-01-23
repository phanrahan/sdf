from sdf import *
from quadrics import double_cone

R = 25.
SHELL = .15*R
SMOOTH = 1.

s = sphere(R).shell(SHELL)

f = s - double_cone().k(SMOOTH)
f &= slab(x0=-2*R, x1=0)

#f.save('baseball.stl')

g = s & (double_cone().rotate(pi /2, X).k(SMOOTH))

baseball = f | g

#baseball.save('baseball.stl', samples=256**3)
baseball.save('baseball.stl', step=(0.2, 0.2, 0.2), bounds=((-30,-30,-30),(30,30,30)))
