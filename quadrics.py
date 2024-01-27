from math import sqrt
import numpy as np
from sdf import sdf3

def _length(a):
    return np.linalg.norm(a, axis=1)

@sdf3
def double_cone(z0=None):
    if z0 is None:
       z0 = 1.0
    def f(p):
        return _length(p[:,[0,1]]) - np.abs(p[:,2]/z0)
    return f

