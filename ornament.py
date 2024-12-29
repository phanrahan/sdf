import fire
from math import pi
from sdf import plane, slab, sphere, rectangle, X, Y, Z
from quadrics import double_cone
from ops import fan, slices, groove, place

R = 25
N = 24
G = 0.25
SHELL = .15
SMOOTH = 1.

class App(object):
    def sphere(self, r):
        self._R = r
        self._s = sphere(r)
        return self

    def rhumb(self, n, g):
        print("rhumb", n)
        f = fan(n)
        diag1 = f.rhumb( pi/4).scale(self._R)
        diag2 = f.rhumb(-pi/4).scale(self._R)
        vgroove = rectangle(g).rotate(pi/4)
        self._s = groove(self._s, diag1.orient(X), vgroove)
        self._s = groove(self._s, diag2.orient(X), vgroove)
        return self

    def diamond(self, n, g):
        f = fan(n)
        diag1 = f.twist( pi).scale(self._R)
        diag2 = f.twist(-pi).scale(self._R)
        vgroove = rectangle(g).rotate(pi/4)
        self._s = groove(self._s, diag1.orient(X), vgroove)
        self._s = groove(self._s, diag2.orient(X), vgroove)
        return self

    def triangle(self, n, g):
        self.diamond(n, g)
        vgroove = rectangle(g).rotate(pi/4)
        self._s = groove(self._s, fan(2*n).orient(X), vgroove)
        return self

    def hex(self, n, g):
        f = fan(n)
        diag1 = f.twist( pi/2).scale(self._R)
        diag2 = f.twist(-pi/2).scale(self._R)
        vgroove =  rectangle(g).rotate(pi/4)
        self._s = groove(self._s, diag1.orient(X), vgroove)
        self._s = groove(self._s, diag2.orient(X), vgroove)
        self._s = groove(self._s, f.orient(X), vgroove)
        return self

    # place spheres at the intersections of a diamond pattern
    def dots(self, n):
        f = fan(n)
        diag1 = f.twist( pi).scale(self._R)
        diag2 = f.twist(-pi).scale(self._R)
        self._s |= place(self._s, diag1.orient(X), diag2.orient(X), sphere())
        return self

    def baseball(self, shell, smooth):
        # subtract an inner sphere to form shell
        s = self._s - sphere((1-shell)*self._R)

        # remove a double cone oriented in Z, smooth the intersection
        f = s - double_cone().k(smooth)
        # remove positive x halfspace
        f &= slab(x0=-2*self._R, x1=0)

        # form a double cone shaped cap oriented along Y
        g = s & (double_cone().orient(Y).k(smooth))

        # return the union of the two pieces
        self._s = f | g
        return self

    def save(self, name):
        s = self._s.translate((0.05,0.05,0.05))
        s.save(name + '.stl', step=(0.1, 0.1, 0.1), bounds=((-30,-30,-30),(30,30,30)))

if __name__ == '__main__':
  app = fire.Fire(App)
