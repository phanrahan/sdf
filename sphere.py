from math import sqrt
import numpy as np
from sdf import *
from quadrics import double_cone
from ops import engrave

_min = np.minimum
_max = np.maximum
_abs = np.abs

R = 25
S = 1.2*R

grooves = plane(Z).repeat((0,0,5))

s = sphere(R)
s = s.engrave(grooves,.2)
s = s.engrave(grooves.rotate(pi/3,X),.2)
s = s.engrave(grooves.rotate(pi/3,Y),.2)

s.save('sphere.stl', step=0.2, bounds=((-S, -S, -S), (S, S, S)))
