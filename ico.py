# https:#www.shadertoy.com/view/wdcczs
# https:#www.shadertoy.com/view/lsV3RV

# icosahedral symmetry
# https:#en.wikipedia.org/wiki/Icosahedral_symmetry

from math import sqrt, tan, pi
from np_sdf import abs, vec3, mat3, matmul
from sdf import sdf3, sphere

PHI = (1.+sqrt(5.))/2.
A = PHI / sqrt( 1. + PHI*PHI )
B = 1. / sqrt( 1. + PHI*PHI )
ICOVERTEX  = vec3(0,A,B)
ICOMIDFACE = vec3(0,A,B)*(1./3.) + vec3(0,0,A)*(2./3.)
ICOMIDEDGE = vec3(0,A,B)*.5 + vec3(B,0,A)*.5

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
def opIcosahedron( p ):
    p = matmul( R0, abs( p ) )
    p = matmul( R1, abs( p ) )
    p = matmul( R2, abs( p ) )
    return abs( p )


# rotate and translate `opIcosahedron` so that
# icosahedron vertex is at origin
# icosahedron edge is negative X-axis
# icosahedron face normal is Z-axis
# icosahedron is in negative Y-space
def opAlignedIcosahedron( p, radius ):
    return matmul( R3, opIcosahedron( p ) ) - O3 * radius

#normalize(vec3(0, 1, PHI+1)),
#normalize(vec3(0, -1, PHI+1)),
#normalize(vec3(PHI+1, 0, 1)),
#normalize(vec3(-PHI-1, 0, 1)),
#normalize(vec3(1, PHI+1, 0)),
#normalize(vec3(-1, PHI+1, 0)),
#
#normalize(vec3(0, PHI, 1)),
#normalize(vec3(0, -PHI, 1)),
#normalize(vec3(1, 0, PHI)),
#normalize(vec3(-1, 0, PHI)),
#normalize(vec3(PHI, 1, 0)),
#normalize(vec3(-PHI, 1, 0))

@sdf3
def icosahedron(fund):
    def f(p):
         return fund(opIcosahedron(p))
    return f

f = sphere(0.1).translate(ICOVERTEX)
#f = sphere(0.1).translate(ICOMIDFACE)
f = icosahedron( f )

D = 2
f.save('ico.stl', step=D/128, bounds=((-D, -D, -D), (D, D, D)))
