# https://github.com/fogleman/sdf/pull/31
#   see also https://nodtem66.github.io/Scaffolder/tutorial_2/

from glsl import np, vec3, abs, min, max, length, cos, sin, cosh, sinh
from sdf import sdf3

#MetaCORE surfaces

@sdf3
def MO(h,slant,size,center = ORIGIN):
    size = vec3(size)
    def f(p):
        x = p[:,0]
        y = p[:,1]
        z = p[:,2]
        d = abs(sin(z)+cos(x+slant*sin(y)))-h
        q = abs(p - center) - size / 2
        return max(d,length(max(q, 0)) + min(np.amax(q, axis=1), 0))
    return f

@sdf3
def EB(h,size,center = ORIGIN):
    size = vec3(size)
    def f(p):
        x = p[:,0]
        y = p[:,1]
        z = p[:,2]
        d = abs(cos(x)+np.cos(y)*np.cos(z))-h
        q = abs(p - center) - size / 2
        return max(d,length(max(q, 0)) + min(np.amax(q, axis=1), 0))
    return f

#Minimal surfaces

@sdf3
def schwarzP(h,size,center = ORIGIN):
    size = vec3(size)
    def f(p):
        x = p[:,0]
        y = p[:,1]
        z = p[:,2]
        d = abs(cos(x)+np.cos(y)+np.cos(z))-h
        q = abs(p - center) - size / 2
        return max(d,length(max(q, 0)) + min(np.amax(q, axis=1), 0))
    return f

@sdf3
def schwarzD(h,size, center = ORIGIN):
    size = vec3(size)
    def f(p):
        x = p[:,0]
        y = p[:,1]
        z = p[:,2]
        d = abs(sin(x)*sin(y)*sin(z)+sin(x)*cos(y)*np.cos(z)+np.cos(x)*sin(y)*np.cos(z))-h
        q = abs(p - center) - size / 2
        return max(d,length(max(q, 0)) + min(np.amax(q, axis=1), 0))
    return f


@sdf3
def gyroid(h,t,size,center = ORIGIN):
    size = vec3(size)
    def f(p):
        x = p[:,0]
        y = p[:,1]
        z = p[:,2]
        d = abs(cos(x)*sin(y)+np.cos(y)*sin(z)+np.cos(z)*sin(x)-t)-h
        q = abs(p - center) - size / 2
        return max(d,length(max(q, 0)) + min(np.amax(q, axis=1), 0))
    return f

@sdf3
#note -- careful with bounds on this one
def scherkSecond(h,size,center = ORIGIN):
    size = vec3(size)
    def f(p):
        x = p[:,0]
        y = p[:,1]
        z = p[:,2]
        d = abs(sin(z)-sinh(x)*sinh(y))-h
        q = abs(p - center) - size / 2
        return max(d,length(max(q, 0)) + min(np.amax(q, axis=1), 0))
    return f
