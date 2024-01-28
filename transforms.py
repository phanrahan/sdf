# coordinate systems

# cylindrical 
def cylindrical(p):
    r = _length(_vec(x,y))
    theta = np.atan2(y,x)

# spherical
def spherical(p):
    r = _length(p)
    theta = np.atan2(y,x)
    phi = np.atan2(_length(_vec(x,y)), z)
    return _vec(theta, phi, r)

def rhumb(p):
    theta = theta - theta0
    phi = arcsinh(tan(phi))
    phi = m * theta where m = cot(beta)

# reflect

# rotate

# translate

# twist/helix

# bend
