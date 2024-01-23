from math import sqrt
import numpy as np
from sdf import *
from quadrics import double_cone
from ops import flatplane, cgroove, vgroove, vemboss, pipe
from ops import circular_array as circular

_min = np.minimum
_max = np.maximum
_abs = np.abs

R = 25
S = 1.2*R
G = 0.2

s = sphere(R)

# doesn't work
#pattern = circular(flatplane(X),10)

# doesn't work
#pattern = flatplane(X).circular_array(10)

n = 10
pattern = flatplane(X)
for i in range(1,n):
    pattern |= pattern.rotate(i*pi/n, Z)
s = s.vemboss(pattern,G)

#pattern = flatplane(Z).repeat((0,0,5))

#s = s.vgroove(pattern,G)
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

s.save('sphere.stl', step=0.2, bounds=((-S, -S, -S), (S, S, S)))
