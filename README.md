# sdf

Experiments using signed distance functions

HG glsl
- https://www.shadertoy.com/view/Xs3GRB

baseball (and other sports balls)
- https://paulbourke.net/geometry/spherical/


# https://www.ronja-tutorials.com/post/035-2d-sdf-combination/#champfer
# https://www.blakecourter.com/2022/06/25/edge-coordinate-system.html
# https://www.blakecourter.com/2022/06/22/constant-width-chamfer.html
# sum (S) is the clearance
# difference (D) is the mid-surface
# two-body = D/S
#
# also intersection_chamfer, difference_chamfer
#@op3
#def union_chamfer(a, b, r):
#    def f(p):
#        d1 = a(p)
#        d2 = b(p)
#        # union( union(a,b), dilate(S(a,b), r))
#        return min(min(d1, d2), (d1 + d2 - r)*sqrt(0.5))
#    return f

# At right-angle intersections between objects,
# build a new local coordinate system from the two distances
# to combine them in interesting ways.
#@op3
#def union_round(a, b, r):
#    def f(p):
#        d1 = a(p)
#        d2 = b(p)
#        u = max(vec(r - d1,r - d2), vec3((0,0)))
#        return max(r, min (d1, d2)) - length(u)
#    return f



#// first object gets a capenter-style tongue attached
#float fOpTongue(float a, float b, float ra, float rb) {
#   union(a, intersection(delate(a, ra), dilate(abs(b), rb))...
    #return min(a, max(a - ra, abs(b) - rb));
#}

