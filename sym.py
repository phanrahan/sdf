from np_sdf import np, abs, min, max, vec3, dot, normalize
from sdf import op3

#def dot(u,v):
#    return np.sum(u*v)
#
#def foldp(p, n):
#    p = np.array(p)
#    n = n/sqrt(dot(n,n))
#    d = min(dot(p,n), 0)
#    p = p - 2. * d * n
#    return p
    
@op3
def fold(other, n=None):
    if n is not None:
        n = normalize(vec3(n))
    def f(p):
        if n is None:
            p = abs(p)
        else:
            d = min(dot(p, n), 0)
            p -= 2 * np.outer(d, n)
        return other(p)
    return f

