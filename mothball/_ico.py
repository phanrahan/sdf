# https:/www.shadertoy.com/view/wdcczs
#define sabs(p) sqrt((p)*(p)+2e-3)
#define smin(a,b) (a+b-sabs(a-b))*.5
#define smax(a,b) (a+b+sabs(a-b))*.5

#float dodec(vec3 p,float r){
#	float G=sqrt(5.)*.5+.5;
#	vec3 n=normalize(vec3(G,1,0));
#	float d=0.;
#    p=sabs(p);
#    d=smax(d,dot(p,n));
#    d=smax(d,dot(p,n.yzx));
#    d=smax(d,dot(p,n.zxy));
#	return d-r;
#}

#float icosa(vec3 p,float r){
#	float G=sqrt(5.)*.5+.5;
#	vec3 n=normalize(vec3(G,1./G,0));
#	float d=0.;
#    p=sabs(p);
#    d=smax(d,dot(p,n));
#    d=smax(d,dot(p,n.yzx));
#    d=smax(d,dot(p,n.zxy));
#	d=smax(d,dot(p,normalize(vec3(1))));
#   return d-r;


# https:/www.shadertoy.com/view/lsV3RV

# https://www.shadertoy.com/view/XlX3zB

# icosahedral symmetry
# https:/en.wikipedia.org/wiki/Icosahedral_symmetry

from math import sqrt, tan, pi
from np_sdf import abs, sign, min, cross, vec3, mat3, matmul
from sdf import sdf3, sphere, capsule, plane, rectangle
from ops import surface, groove
import sym

PHI = (1.+sqrt(5.))/2.
A = PHI / sqrt( 1. + PHI*PHI )
B = 1. / sqrt( 1. + PHI*PHI )
ICOVERTEX  = vec3(0,A,B)
ICOMIDFACE = vec3(0,A,B)*(1./3.) + vec3(0,0,A)*(2./3.)
ICOMIDEDGE = vec3(0,A,B)*.5 + vec3(B,0,A)*.5

V1 = vec3(B,0,A)
V2 = vec3(A,B,0)
V3 = vec3(0,A,B)

J = 0.309016994375
K = J+.5
R0 = mat3(0.5,-K,J  ,K,J,-0.5      ,J,0.5,K                          )
R1 = mat3(K,J,-0.5   ,J,0.5,K      ,0.5,-K,J                         )
R2 = mat3(-J,-0.5,K  ,0.5,-K,-J    ,K,J,0.5                          )

R3 = mat3(-0.5,sqrt(.75),0,K,0.467086179481,0.356822089773,-J,-0.178411044887,0.934172358963)
O3 = vec3(B,B/sqrt(3.),sqrt(1.-4./3.*B*B))

R4 = mat3(0.587785252292,-K,0.,-0.425325404176,-J,0.850650808352,0.688190960236,0.5,0.525731112119)
O4 = vec3(A/3./tan(pi/5.),A/3.,0.63147573033330584)


# opIcosahedron will create 120x symmetry
# All points will be mapped to a single face of a icosahedron (20x symmetry)
# Also, points will be put into 1/6th of that face (addition 6x symmetry)
#
# The icosahedron face vertices are vec3(0,A,B), vec3(B,0,A), vec3(-B,0,A)
#
# return value will be between these rays:
#    vertex:        vec3(0,A,B)
#    face midpoint: vec3(0,A,B)*(1./3.) + vec3(0,0,A)*(2./3.)
#    edge midpoint: vec3(0,A,B)*.5 + vec3(B,0,A)*.5
#
# this is equivalent to dodecahedral symmetry (12x faces, 10x within face)
# (formula by DjinnKahn)
def opFullIcosahedron( p ):
    p = matmul( R0, abs( p ) )
    p = matmul( R1, abs( p ) )
    p = matmul( R2, abs( p ) )
    return abs( p )

# same as opIcosahedron, except without mirroring symmetry, so X-coordinate may be negative
# (note: when this is used as a distance function, it's possible that the nearest object is
# on the opposite polarity, potentially causing a glitch)
def opIcosahedron( p ):
    pol = sign( p )
    p = matmul( R0, abs( p ) )
    pol *= sign( p )
    p = matmul( R1, abs( p ) )
    pol *= sign( p )
    p = matmul( R2, abs( p ) )
    pol *= sign( p )
    ret1 = abs( p )
    ret2 = ret1
    ret2[:,0] = pol[:,0] * pol[:,1] * pol[:,2] * ret1[:,0]
    return min(ret1,ret2)


# rotate and translate `opIcosahedron` so that
# icosahedron vertex is at origin
# icosahedron edge is negative X-axis
# icosahedron face normal is Z-axis
# icosahedron is in negative Y-space
def opAlignedIcosahedron( p, radius ):
    return matmul( R3, opIcosahedron( p ) ) - O3 * radius

@sdf3
def fullicosahedron(fund):
    def f(p):
         return fund(opIcosahedron(p))
    return f


def ico(fund):
    return fund.fold(cross(V1,V2)).fold(cross(V2,V3)).fold(cross(V3,V1)).fold()
    #return fund.fold(V2-V1).fold().fold(V3-V2).fold().fold(V1-V3).fold()

R = 25
G = 2

e1 = surface(plane(cross(V1, V2)))
e2 = surface(plane(cross(V2, V3)))
e3 = surface(plane(cross(V3, V1)))
e = e1 | e3 | e2
g = rectangle(G).rotate(pi/4)
s = groove(sphere(R),e,g)

#s1 = sphere(0.1).translate(V1)
#s2 = sphere(0.1).translate(V2)
#s3 = sphere(0.1).translate(V3)
#s1 = capsule(V1, V2,0.1)
#s2 = capsule(V2, V3,0.1)
#s3 = capsule(V3, V1,0.1)
#s = s1 | s2 | s3

s = ico(s)

D = R+5
step = D/128
s.translate((step/2,step/2,step/2)).save('ico.stl', step=step, bounds=((-D, -D, -D), (D, D, D)))
