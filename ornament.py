import fire
from math import pi
from sdf import plane, slab, sphere, rectangle, X, Y, Z
from quadrics import double_cone
from ops import fan, slices, groove


class App(object):
    def __init__(self, r=25, n=24, g=.25):
        self.R = r
        self.N = n
        self.G = g
        self.SHELL = .15
        self.SMOOTH = 1.

        self.s = sphere(self.R)
        self.groove =  rectangle(self.G).rotate(pi/4)

    def ball(self):
        self.name = 'ball'

    def diamond(self):
        f = fan(self.N)
        diag1 = f.twist( pi).scale(self.R)
        diag2 = f.twist(-pi).scale(self.R)
        self.s = groove(self.s, diag1.orient(X), self.groove)
        self.s = groove(self.s, diag2.orient(X), self.groove)
        self.name = 'diamond'

    def triangle(self):
        self.diamond()
        self.s = groove(self.s, fan(2*self.N).orient(X), self.groove)
        self.name = 'triangle'

    def hex(self):
        f = fan(self.N)
        diag1 = f.twist( pi/2).scale(self.R)
        diag2 = f.twist(-pi/2).scale(self.R)
        self.s = groove(self.s, diag1.orient(X), self.groove)
        self.s = groove(self.s, diag2.orient(X), self.groove)
        self.s = groove(self.s, f.orient(X), self.groove)
        self.name = 'hex'

    def baseball(self):
        # subtract an inner sphere to form shell
        self.s = self.s - sphere((1-self.SHELL)*self.R)

        # remove a double cone oriented in Z, smooth the intersection
        f = self.s - double_cone().k(self.SMOOTH)
        # remove positive x halfspace
        f &= slab(x0=-2*self.R, x1=0)

        # form a double cone shaped cap oriented along Y
        g = self.s & (double_cone().orient(Y).k(self.SMOOTH))

        # return the union of the two pieces
        self.s = f | g

    def exit(self):
        self.s = self.s.translate((0.05,0.05,0.05))
        self.s.save(self.name + '.stl', step=(0.1, 0.1, 0.1), bounds=((-30,-30,-30),(30,30,30)))

if __name__ == '__main__':
  app = App()
  fire.Fire(app)
  app.baseball()
  app.exit()
