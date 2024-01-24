from math import sqrt
import numpy as np
from sdf import *

def _length(a):
    return np.linalg.norm(a, axis=1)

@sdf3
def double_cone(k=None):
    if k is None:
       k = 1.0
    def f(p):
        return _length(p[:,[0,1]]) - k*np.abs(p[:,2])
    return f

