from sdf import *

f = capped_cylinder(-4*Z, 4*Z, 0.5).translate((0.5,0,0)).twist(2*pi)

f.save('rope.stl')
