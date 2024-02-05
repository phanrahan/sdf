import numpy as np

min = np.minimum
max = np.maximum
abs = np.absolute
sign = np.sign

sin = np.sin
cos = np.cos
tan = np.tan
#cot = np.cot
atan = np.arctan
atan2 = np.arctan2

sinh = np.sinh
cosh = np.cosh
tanh = np.tanh
arcsinh = np.arcsinh
arccosh = np.arccosh
artansh = np.arctanh

exp = np.exp
log = np.log

def normalize(a):
    return a / np.linalg.norm(a)

def length(a):
    return np.linalg.norm(a, axis=1)

def dot(a, b):
    return np.sum(a * b, axis=1)

def cross(a,b):
    return np.cross(a,b)

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

# numpy funkiness to convert 2 signed distance calculations to a vector
def vec2d(d1,d2):
    return vec(d1.reshape(-1),d2.reshape(-1))

# numpy funkiness to convert 3 signed distance calculations to a vector
def vec3d(d1,d2,d3):
    return vec(d1.reshape(-1),d2.reshape(-1),d3.reshape(-1))


def mat3(*m):
    return np.array(m).reshape(3,3)

def matmul(m, p):
    return (m @ p.transpose()).transpose()

def smoothstep (x):
    return x * x * (3.0 - 2.0 * x);

def clamp(x, min=0., max=1.):
    return np.where(x < min, min, np.where(x > max, max, x))

