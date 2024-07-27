import numpy as np
from glsl import vec3, normalize, length
from sdf import sphere

v = vec3(1,1,1)
#print(v)
#print(normalize(v))

# points are n x 3 arrays
p = np.array([[0,0,0],[1,0,0],[1,1,1]])
q = np.array([[1,1,1]])


print(p)
print(p-v)
print(p-1)
print(p-[1])
print(p-[[1]])
print(p-[1,1,1])
print(p-[[1,1,1]])
#print(length(p))
#print(np.linalg.norm(p))
#print(normalize(p))
#print(normalize(q))

#s = sphere()
# distances are n x 1 arrays
#print(s(p))
