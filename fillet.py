from sdf import union, sphere, box, rounded_box
from ops import fillet

R = 25
G = 5

s = sphere(R)
b = box(R).translate((R,0,0))
#b = rounded_box(R,G).translate((R,0,0))

#r = fillet(s, b, 5)
#r = b.erode(G)
r = b
#r = union(s.erode(G), b.erode(5))

r.save('fillet.stl', step=0.2, bounds=((-30, -30, -30), (30, 30, 30)))
