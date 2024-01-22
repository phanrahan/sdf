from sdf import *

@sdf3
def double_cone():
    def f(p):
        x = p[:,0]
        y = p[:,1]
        z = p[:,2]
        return x*x+y*y-z*z
    return f

