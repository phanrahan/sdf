from math import sqrt
import numpy as np
from sdf import union, plane, sphere, cylinder, X, Y, Z, pi
from quadrics import double_cone
from ops import surface, vgroove, vemboss

_min = np.minimum
_max = np.maximum
_abs = np.abs

R = 25
G = 0.25
N = 36


def fan(n):
    return plane(Y).surface().circular_array(n)

def slices(d):
    return plane(Z).surface().repeat((0,0,d))

def viviani(r, n):
    c = cylinder(r).surface().translate((r,0,0))
    return union(c, *[c.rotate(2*pi*i/n, Z) for i in range(1,n)])

long = fan(N)
lat = slices(2*R/N)
viv = viviani(R/2, N)

s = sphere(R)

#s = s.vgroove(lat,G)
#s = s.vgroove(lat.orient(X),G)
#s = s.vgroove(lat.orient(Y),G)

s = s.vgroove(viv, G)

#s = s.vgroove(long,G)
#s = s.vgroove(long.orient(X),G)
#s = s.vgroove(long.orient(Y),G)

s.save('sphere.stl', step=0.2, bounds=((-30, -30, -30), (30, 30, 30)))
