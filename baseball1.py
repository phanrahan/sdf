from sdf import *
from quadrics import double_cone
from ops import surface

R = 25.
SHELL = .15*R
SMOOTH = 1.
G = 0.5
N = 48

def slices(d):
    return plane(Z).surface().repeat((0,0,d))


s = sphere(R) 

lat = slices(4*R/N)

s = s.vgroove(lat,G)
#s = s.vgroove(lat.rotate( pi/3, X),G)
#s = s.vgroove(lat.rotate( pi/3, Y),G)

s = s - sphere(R-SHELL)

# cone along Z 
f = s - double_cone().k(SMOOTH)
f &= slab(x0=-2*R, x1=0)

#f.save('baseball.stl')

# cone along Y
g = s & (double_cone().orient(Y).k(SMOOTH))

baseball = f | g

baseball = baseball.translate((0.1,0.1,0.1))
baseball.save('baseball1.stl', step=(0.2, 0.2, 0.2), bounds=((-30,-30,-30),(30,30,30)))
