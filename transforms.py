import numpy as np
from sdf import op3

# coordinate systems

# cylindrical 
#def cylindrical(p):
#    r = _length(_vec(x,y))
#    theta = np.atan2(y,x)

# spherical
#def spherical(p):
#    r = _length(p)
#    theta = np.atan2(y,x)
#    phi = np.atan2(_length(_vec(x,y)), z)

# reflect

# rotate

# translate

# twist/helix

# bend

def _vec(*arrs):
    return np.stack(arrs, axis=-1)

def smoothstep (x):
    return x * x * (3.0 - 2.0 * x);

def clamp(x, min=0., max=1.):
    return np.where(x < min, min, np.where(x > max, max, x))

@op3
def twist(other, k):
    def f(p):
        x = p[:,0]
        y = p[:,1]
        z = p[:,2]
        #a = k*smoothstep(clamp(1-abs(z)))
        a = k*clamp(1-abs(z))
        c = np.cos(a)
        s = np.sin(a)
        x2 = c * x - s * y
        y2 = s * x + c * y
        z2 = z
        return other(_vec(x2, y2, z2))
    return f

