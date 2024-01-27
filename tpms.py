# https://github.com/fogleman/sdf/pull/31
#   see also https://nodtem66.github.io/Scaffolder/tutorial_2/

import numpy as np
from sdf import *

_min = np.minimum
_max = np.maximum

def _length(a):
    return np.linalg.norm(a, axis=1)

#MetaCORE surfaces

@sdf3
def MO(h,slant,size,center = ORIGIN):
    size = np.array(size)
    def f(p):
        x = p[:,0]
        y = p[:,1]
        z = p[:,2]
        d = np.abs(np.sin(z)+np.cos(x+slant*np.sin(y)))-h
        q = np.abs(p - center) - size / 2
        return _max(d,_length(_max(q, 0)) + _min(np.amax(q, axis=1), 0))
    return f

@sdf3
def EB(h,size,center = ORIGIN):
    size = np.array(size)
    def f(p):
        x = p[:,0]
        y = p[:,1]
        z = p[:,2]
        d = np.abs(np.cos(x)+np.cos(y)*np.cos(z))-h
        q = np.abs(p - center) - size / 2
        return _max(d,_length(_max(q, 0)) + _min(np.amax(q, axis=1), 0))
    return f

#Minimal surfaces

@sdf3
def schwarzP(h,size,center = ORIGIN):
    size = np.array(size)
    def f(p):
        x = p[:,0]
        y = p[:,1]
        z = p[:,2]
        d = np.abs(np.cos(x)+np.cos(y)+np.cos(z))-h
        q = np.abs(p - center) - size / 2
        return _max(d,_length(_max(q, 0)) + _min(np.amax(q, axis=1), 0))
    return f

@sdf3
def schwarzD(h,size, center = ORIGIN):
    size = np.array(size)
    def f(p):
        x = p[:,0]
        y = p[:,1]
        z = p[:,2]
        d = np.abs(np.sin(x)*np.sin(y)*np.sin(z)+np.sin(x)*np.cos(y)*np.cos(z)+np.cos(x)*np.sin(y)*np.cos(z))-h
        q = np.abs(p - center) - size / 2
        return _max(d,_length(_max(q, 0)) + _min(np.amax(q, axis=1), 0))
    return f


@sdf3
def gyroid(h,t,size,center = ORIGIN):
    size = np.array(size)
    def f(p):
        x = p[:,0]
        y = p[:,1]
        z = p[:,2]
        d = np.abs(np.cos(x)*np.sin(y)+np.cos(y)*np.sin(z)+np.cos(z)*np.sin(x)-t)-h
        q = np.abs(p - center) - size / 2
        return _max(d,_length(_max(q, 0)) + _min(np.amax(q, axis=1), 0))
    return f

@sdf3
#note -- careful with bounds on this one
def scherkSecond(h,size,center = ORIGIN):
    size = np.array(size)
    def f(p):
        x = p[:,0]
        y = p[:,1]
        z = p[:,2]
        d = np.abs(np.sin(z)-np.sinh(x)*np.sinh(y))-h
        q = np.abs(p - center) - size / 2
        return _max(d,_length(_max(q, 0)) + _min(np.amax(q, axis=1), 0))
    return f
