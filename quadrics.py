from math import sqrt
from np_sdf import abs, length
from sdf import sdf3

@sdf3
def double_cone(z0=None):
    if z0 is None:
       z0 = 1.0
    def f(p):
        return length(p[:,[0,1]]) - abs(p[:,2]/z0)
    return f

