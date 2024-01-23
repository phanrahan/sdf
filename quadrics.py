import numpy as np
from sdf import *

def _length(a):
    return np.linalg.norm(a, axis=1)

@sdf3
def double_cone():
    def f(p):
        return _length(p[:,[0,1]]) - np.abs(p[:,2])
    return f

