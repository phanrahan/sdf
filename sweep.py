from sdf import plane, sphere, circle, X, Y, Z
import ops

R = 25

s = sphere(R)
p = plane(Z)
c = circle()

s = s.sweep(p, c)

s.save('sweep.stl', step=0.2, bounds=((-30, -30, -30), (30, 30, 30)))
