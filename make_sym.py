import fire
from math import pi, sqrt
from glsl import vec3, cross
from sdf import sphere, rectangle
from ops import groove
from sym import subdivide, triangle

R = 25
G = 1
N = 0

class App(object):
    def __init__(self):
        self.name = None

    def tet(self, r=R, g=G, n=N):
        self.name = 'tet'
        self.R = r
        self.G = g
        self.N = n
        V1 = vec3( 1,-1, 1)
        V2 = vec3( 1, 1,-1)
        V3 = vec3(-1, 1, 1)
        #V1 = vec3(-1,-1, 1)
        #V2 = vec3( 1,-1,-1)
        #V3 = vec3(-1, 1,-1)
        self.e = subdivide(V1, V2, V3, self.N)
        self.e = self.e.fold(cross(V1,V2)).fold(cross(V2,V3)).fold(cross(V3,V1))
        print(cross(V1,V2))
        print(cross(V2,V3))
        print(cross(V3,V1))
        #self.e = self.e.fold(vec3(1,1,0)).fold(vec3(0,1,1)).fold(vec3(1,0,1))
        # planes formed by one edge and the midpoint of the ooposite edge

    def oct(self, r=R, g=G, n=N):
        self.name = 'oct'
        self.R = r
        self.G = g
        self.N = n
        V1 = vec3(1,0,0)
        V2 = vec3(0,1,0)
        V3 = vec3(0,0,1)
        self.e = subdivide(V1, V2, V3, self.N)
        self.e = self.e.fold_xyz()

    def ico(self, r=R, g=G, n=N):
        self.name = 'ico'
        self.R = r
        self.G = g
        self.N = n
        PHI = (1.+sqrt(5.))/2.
        A = PHI / sqrt( 1. + PHI*PHI )
        B = 1. / sqrt( 1. + PHI*PHI )
        V1 = vec3(B,0,A)
        V2 = vec3(A,B,0) 
        V3 = vec3(0,A,B) 
        self.e = subdivide(V1, V2, V3, self.N)
        self.e = self.e.fold(cross(V1,V2)).fold(cross(V2,V3)).fold(cross(V3,V1)).fold_xyz()


    def exit(self):
        if self.name:

            #self.s = sphere(self.R)
            #self.g =  rectangle(self.G).rotate(pi/4)
            #s = groove(self.s, self.e, self.g)
            s = self.e

            D = self.R+5
            step = D/256
            filename = self.name + str(self.N) + '.stl'
            print('saving', filename)
            s.translate((step/2,step/2,step/2)).save(filename, step=step, bounds=((-D, -D, -D), (D, D, D)))

if __name__ == '__main__':
  app = App()
  fire.Fire(app)
  app.exit()

