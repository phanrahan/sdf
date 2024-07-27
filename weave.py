from math import sqrt
from glsl import vec3
from sdf import rounded_box, cylinder, slab, ease, X, Y, Z

root3 = sqrt(3.0)
s = 2.7
unit = s * vec3((1,root3,0))


f = rounded_box([3.2, 1, 0.25], 0.1).translate((1.5, 0, 0.0625))
f = f.bend_linear(X * 0.75, X * 2.25, Z * -0.1875, ease.in_out_quad)
f = f.circular_array(3, 0)

f = f.repeat(unit, padding=1)
f |= f.translate(unit/2)

f &= cylinder(10)
f |= (cylinder(12) - cylinder(10)) & slab(z0=-0.5, z1=0.5).k(0.25)

f.save('weave.stl')
