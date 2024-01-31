import numpy as np

min = np.minimum
max = np.maximum
abs = np.absolute
sin = np.sin
cos = np.cos
atan2 = np.arctan
sinh = np.sinh
cosh = np.cosh
exp = np.exp
log = np.log

def normalize(a):
    return a / np.linalg.norm(a)

def length(a):
    return np.linalg.norm(a, axis=1)

def dot(a, b):
    return np.sum(a * b, axis=1)

def perpendicular(v):
    if v[1] == 0 and v[2] == 0:
        if v[0] == 0:
            raise ValueError('zero vector')
        else:
            return np.cross(v, [0, 1, 0])
    return np.cross(v, [1, 0, 0])

def vec(*arrs):
    return np.stack(arrs, axis=-1)

def vec3(*p):
    return np.array(p)

def mat3(*m):
    return np.array(m).reshape(3,3)

def matmul(m, p):
    return (m @ p.transpose()).transpose()

def smoothstep (x):
    return x * x * (3.0 - 2.0 * x);

def clamp(x, min=0., max=1.):
    return np.where(x < min, min, np.where(x > max, max, x))

