from math import pi
from sdf import union, plane, sphere, cylinder, rectangle, X, Y, Z
from quadrics import double_cone
from ops import fan, slices, surface, groove, emboss, place, rhumb

R = 25
N = 18
G = rectangle(2).rotate(pi/4)

def viviani(r, n):
    c = cylinder(r).surface().translate((r,0,0))
    return union(c, *[c.rotate(2*pi*i/n, Z) for i in range(1,n)])

long = fan(N)
lat = slices(2*R/N)
viv = viviani(R/2, N)

#diag1 = fan(N).twist( pi/2).scale(R)
#diag2 = fan(N).twist(-pi/2).scale(R)

rhumb1 = fan(N).rhumb( pi/4)
rhumb2 = fan(N).rhumb(-pi/4)

s = sphere(R)

#s = groove(s, plane(Z), G)

#s = groove(s,lat,G)
#s = groove(s,long,G)

#s |= place(s,lat,long, sphere(0.5))

s = groove(s,rhumb1|rhumb2,G)

#s = groove(s,diag1,G)
#s = groove(s,diag2,G)

#s = groove(s,lat,G)
#s = groove(s,lat.orient(X),G)
#s = groove(s,lat.orient(Y),G)

#s = groove(s,viv, G)

#s = groove(s,long,G)
#s = groove(s,long.orient(X),G)
#s = groove(s,long.orient(Y),G)

s.save('sphere.stl', step=0.2, bounds=((-30, -30, -30), (30, 30, 30)))
