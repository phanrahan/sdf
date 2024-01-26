from math import sqrt
import numpy as np
from sdf import sphere, X, Y, Z, pi
from quadrics import double_cone
from ops import flatplane, cgroove, vgroove, vemboss

_min = np.minimum
_max = np.maximum
_abs = np.abs

R = 25
S = 1.2*R
G = 0.5
N = 36


def fan(n):
    return flatplane(Y).circular_array(n)

def slices(d):
    return flatplane(Z).repeat((0,0,d))

long = fan(N)
lat = slices(4*R/N)

s = sphere(R)

#s = s.vgroove(lat,G)
#s = s.vgroove(lat.orient(X),G)
#s = s.vgroove(lat.orient(Y),G)

s = s.vgroove(long,G)
s = s.vgroove(long.orient(X),G)
s = s.vgroove(long.orient(Y),G)

#s = s.vgroove(long.rotate(-pi/3, X).translate((0,0,R)),G)
#s = s.vgroove(long.rotate( pi/3, X).translate((0,0,R)),G)

#s = s.vgroove(lat,G)
#s = s.vgroove(lat.rotate( pi/3, X),G)
#s = s.vgroove(lat.rotate(-pi/3, X),G)

#s = s.vgroove(pattern.rotate(pi/2,X),G)
#s = s.vgroove(pattern.rotate(pi/2,Y),G)

#s = s.vgroove(pattern,G)
#s = s.vgroove(pattern.rotate(pi/3,X),G)
#s = s.vgroove(pattern.rotate(pi/3,Y),G)

s.save('sphere.stl', step=0.2, bounds=((-30, -30, -30), (30, 30, 30)))
