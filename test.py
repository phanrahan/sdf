from sdf import union, intersection, difference, sphere, box, circle, rectangle
from ops import union_round, intersection_round, sweep
import numpy as np
from np_sdf import length

p = np.array([[0,0,0],[1,0,0],[1,1,1]])

s = sphere()

# 1d
print(p[:,0])
# 1d
print(length(p)-1)
# 2d
print(s(p))
# 1d
print(s(p).reshape(-1))
