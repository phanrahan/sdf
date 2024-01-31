from math import sqrt
from sdf import sphere, plane, slab, X, Y, Z, pi
from quadrics import double_cone

R = 25.
SHELL = 0.15*R
SMOOTH = 1.

s = sphere(R) - sphere(R-SHELL)

# cone tip at the north and south poles
r = sqrt(2)/2
r = r / (r + 1) # scale z so the radius at the intersection is sqrt(2)/2
c1 = double_cone(r).translate((0,0,-R)) & plane( Z)
c2 = double_cone(r).translate((0,0, R)) & plane(-Z)
c = c1 | c2
f = s - c
f &= slab(x0=-2*R, x1=0)

#f.save('baseball.stl')

c1 = double_cone(r).translate((0,0,-R)).rotate(pi /2, X) & plane(-Y)
c2 = double_cone(r).translate((0,0, R)).rotate(pi /2, X) & plane( Y)
c = c1 | c2
#g = f & c 
g = s & c - slab(x0=-2*R, x1=0)

baseball = f | g

#baseball = f | g.k(4.)
#baseball &= s

# offset by 1/2 step
baseball = baseball.translate([.1,.1,.1])
baseball.save('baseball2.stl', step=(0.2, 0.2, 0.2), bounds=((-30,-30,-30),(30,30,30)))
