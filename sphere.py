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

s = sphere(R)

# radial grooves

pattern = flatplane(Y).circular_array(N)

#n = 10
#pattern = flatplane(X)
#for i in range(1,n):
    #pattern |= pattern.rotate(i*pi/n, Z)

s = s.vgroove(pattern,G)
#s = s.vemboss(pattern,G)

# fails
#s = s.cgroove(pattern,G)

# fails
#s = s.pipe(pattern,G)

# parallel grooves

pattern = flatplane(Z).repeat((0,0,4*R/N))

s = s.vgroove(pattern,G)

#s = s.vgroove(pattern.rotate(pi/2,X),G)
#s = s.vgroove(pattern.rotate(pi/2,Y),G)

#s = s.vemboss(pattern,G)
#s = s.vemboss(pattern.rotate(pi/2,X),G)
#s = s.vemboss(pattern.rotate(pi/2,Y),G)

#s = s.vgroove(pattern,G)
#s = s.vgroove(pattern.rotate(pi/3,X),G)
#s = s.vgroove(pattern.rotate(pi/3,Y),G)

#s = s.vemboss(pattern,G)
#s = s.vemboss(pattern.rotate(pi/3,X),G)
#s = s.vemboss(pattern.rotate(pi/3,Y),G)

# doesn't work
#s = s.cgroove(pattern,G)
#s = s.cgroove(pattern.rotate(pi/3,X),G)
#s = s.cgroove(pattern.rotate(pi/3,Y),G)

# doesn't work - fails in _vec
#s = s.pipe(pattern,G)
#s = s.pipe(pattern.rotate(pi/3,X),G)
#s = s.pipe(pattern.rotate(pi/3,Y),G)

s.save('sphere.stl', step=0.2, bounds=((-30, -30, -30), (30, 30, 30)))
