from sdf import *
from quadrics import double_cone
from ops import fan, slices, surface

R = 25.
SHELL = .15*R
SMOOTH = 1.
G = 0.25
N = 48

def viviani(r, n):
    c = cylinder(r).surface().orient(Y).translate((r,0,0))
    return union(c, *[c.rotate(2*pi*i/n, Y) for i in range(1,n)])

s = sphere(R) 

#lat = slices(4*R/N)

#s = s.vgroove(lat,G)
#s = s.vgroove(lat.rotate( pi/3, X),G)
#s = s.vgroove(lat.rotate( pi/3, Y),G)

#diamond
f = fan(N)
diag1 = f.twist( pi).scale(R)
diag2 = f.twist(-pi).scale(R)
#diag1 = f.twist( pi/2).scale(R)
#diag2 = f.twist(-pi/2).scale(R)
s = s.vgroove(diag1.orient(Y), G)
s = s.vgroove(diag2.orient(Y), G)

#triangle
#s = s.vgroove(fan(2*N).orient(Y), G)

#hex
#f = fan(N/2)
#diag1 = f.twist( pi/2).scale(R)
#diag2 = f.twist(-pi/2).scale(R)
#s = s.vgroove(diag1.orient(Y), G)
#s = s.vgroove(diag2.orient(Y), G)
#s = s.vgroove(fan(N).rotate(pi/N, Z).orient(Y), G)

#s = s.vgroove(viviani((1+2*G)*R/2, 2*N).rotate(pi/2, Z), G)

s = s - sphere(R-SHELL)

# cone along Z 
f = s - double_cone().k(SMOOTH)
f &= slab(x0=-2*R, x1=0)

#f.save('baseball.stl')

# cone along Y
g = s & (double_cone().orient(Y).k(SMOOTH))

baseball = f | g

baseball = baseball.translate((0.05,0.05,0.05))
baseball.save('baseball1.stl', step=(0.2, 0.2, 0.2), bounds=((-30,-30,-30),(30,30,30)))
