# https://www.shadertoy.com/view/wdcczs
# https://www.shadertoy.com/view/lsV3RV

# icosahedral symmetry
# https://en.wikipedia.org/wiki/Icosahedral_symmetry

from math import sqrt

PHI = 0.5 * (1.0 + sqrt(5))

normalize(vec3(0, 1, PHI+1)),
normalize(vec3(0, -1, PHI+1)),
normalize(vec3(PHI+1, 0, 1)),
normalize(vec3(-PHI-1, 0, 1)),
normalize(vec3(1, PHI+1, 0)),
normalize(vec3(-1, PHI+1, 0)),

normalize(vec3(0, PHI, 1)),
normalize(vec3(0, -PHI, 1)),
normalize(vec3(1, 0, PHI)),
normalize(vec3(-1, 0, PHI)),
normalize(vec3(PHI, 1, 0)),
normalize(vec3(-PHI, 1, 0))
