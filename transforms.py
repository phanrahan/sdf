from glsl import np, vec, length, tan, cot, atan2, arcsinh, clamp, smoothstep
from sdf import op3

# coordinate systems

# cylindrical 
def cylindrical(p):
    r = length(vec(x,y))
    theta = atan2(y,x)

def spherical(p):
    r = length(p)
    theta = atan2(y,x)
    phi = atan2(length(vec(x,y)), z)

def rhumb(p):
    pass
    #theta = theta - theta0
    #phi = arcsinh(tan(phi))
    #phi = m * theta where m = cot(beta)

# reflect

# rotate

# translate

# twist/helix

# bend

@op3
def spherical_twist(other, k):
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

