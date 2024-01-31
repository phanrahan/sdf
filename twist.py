from math import pi
from sdf import box

s = box((1,0.02,1)).twist(pi/2)

s.save('twist.stl')
