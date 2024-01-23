from sdf import *
from minimal import schwarzP

f = schwarzP(0,1) 

f.save('schwarzp.stl', bounds=((-1,-1,-1), (1,1,1)))
