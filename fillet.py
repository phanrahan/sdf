from sdf import union, intersection, difference, sphere, box, circle, rectangle
from ops import union_round, intersection_round, sweep

R = 25
G = 2

#a = sphere(R)
a = box(2*R)
b = box(R).translate((R,0,0))

r = union_round(a, b, G)
#u = union(a,b)
#c = rectangle(G).translate((G/2,G/2))-circle(G).translate((G,G))
#f = sweep(a, b, c)
#r = union(u, f)

#r = intersection_round(a, b, G)
#u = intersection(a,b)
#c = rectangle(G).translate((-G/2,-G/2))-circle(G).translate((-G,-G))
#f = sweep(a, b, c)
#r = u-f

r.save('fillet.stl', step=0.1, bounds=((-60, -60, -60), (60, 60, 60)))
