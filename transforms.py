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

# reflect

# rotate

# translate

# twist/helix

# bend
