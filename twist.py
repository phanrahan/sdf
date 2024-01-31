from math import sqrt
import numpy as np
from sdf import op3, union, plane, sphere, cylinder, box, X, Y, Z, pi
from transforms import twist

s = box((1,0.02,1)).twist(pi/2)

s.save('twist.stl')
