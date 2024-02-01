from math import pi
from sdf import plane, sphere, circle, hexagon, rectangle, X, Y, Z
from quadrics import double_cone
from ops import pipe, groove, emboss

R = 25

s = sphere(R)
#p = plane(Z)
p = double_cone()
c = circle()
#c = hexagon(1)
#c = rectangle().rotate(pi/4)

#s -= s.sweep(p, c)
#s -= pipe(s, p)
#s = groove(s, p, c)
s = emboss(s, p, c)

s.save('sweep.stl', step=0.2, bounds=((-30, -30, -30), (30, 30, 30)))
