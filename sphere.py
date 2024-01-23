from math import sqrt
import numpy as np
from sdf import *
from quadrics import double_cone
from ops import engrave

_min = np.minimum
_max = np.maximum
_abs = np.abs

grooves = plane(Z).repeat((0,0,1))

s = sphere(10)
s = s.engrave(grooves,.2)
s = s.engrave(grooves.rotate(pi/3,X),.2)
s = s.engrave(grooves.rotate(pi/3,Y),.2)

s.save('sphere.stl', samples=256**3)
