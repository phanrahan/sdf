from sdf import slab
from quadrics import double_cone

quad = double_cone()
f = quad & slab(z0=-1.0, z1=1.0)

#f.save('cone.stl')
#f.save('cone.stl', bounds=((-1.2, -1.2, -1.2), (1.2, 1.2, 1.2)))
f.show_slice(x=0, bounds=((-1.2, -1.2, -1.2), (1.2, 1.2, 1.2)))

