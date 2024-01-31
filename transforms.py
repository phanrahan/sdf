from np_sdf import np, length, clamp, smoothstep
from sdf import op3

# coordinate systems

# cylindrical 
#def cylindrical(p):
#    r = length(_vec(x,y))
#    theta = np.atan2(y,x)

# spherical
#def spherical(p):
#    r = length(p)
#    theta = np.atan2(y,x)
#    phi = np.atan2(_length(_vec(x,y)), z)

# reflect

# rotate

# translate

# twist/helix

# bend

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


#m = np.array([
#    [1-2*x*x,  -2*x*y,  -2*x*z],
#    [ -2*x*y, 1-2*y*y,  -2*y*z],
#    [ -2*x*z,  -2*y*z, 1-2*z*z],
#    ]).T
#p = np.dot(p, m)

