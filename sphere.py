from math import pi, sqrt
from sdf import union, plane, sphere, cylinder, X, Y, Z
from quadrics import double_cone
from ops import fan, slices, surface, vgroove, vemboss

R = 25
G = 0.25
N = 36

def viviani(r, n):
    c = cylinder(r).surface().translate((r,0,0))
    return union(c, *[c.rotate(2*pi*i/n, Z) for i in range(1,n)])

long = fan(N)
lat = slices(2*R/N)
viv = viviani(R/2, N)

diag1 = fan(N).twist( pi/2).scale(R)
diag2 = fan(N).twist(-pi/2).scale(R)

s = sphere(R)

s = s.vgroove(diag1,G)
s = s.vgroove(diag2,G)

#s = s.vgroove(lat,G)
#s = s.vgroove(lat.orient(X),G)
#s = s.vgroove(lat.orient(Y),G)

#s = s.vgroove(viv, G)

#s = s.vgroove(long,G)
#s = s.vgroove(long.orient(X),G)
#s = s.vgroove(long.orient(Y),G)

s.save('sphere.stl', step=0.2, bounds=((-30, -30, -30), (30, 30, 30)))
