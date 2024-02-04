import numpy as np
from sdf import sample_slice, sphere

# https://www.shadertoy.com/view/DssczX

# colormap is callable, x=0 to 1, rgba floaats
# counter minor, major
# color a<0, a>0

# color a-b<0, a-b>0

#vec4 strokeImplicit(Implicit a, float width, vec4 base) {
#    vec4 color = vec4(a.Color.rgb * 0.25, a.Color.a);
#
#    float interp = clamp(width * 0.5 - abs(a.Distance) / length(a.Gradient), 0.0, 1.);
#    return mix(base, color, color.a * interp);
#
#    return base;
#}
#
#vec4 drawImplicit(Implicit a, vec4 base) {
#    float bandWidth = 20.0;
#    float falloff = 150.0;
#    float widthThin = 2.0;
#    float widthThick = 4.0;
#
#    vec4 opColor = mix(base, a.Color, (a.Distance < 0.0 ? a.Color.a * 0.1 : 0.0));
#    Implicit wave = TriangleWaveEvenPositive(a, bandWidth, a.Color);
#
#    wave.Color.a = max(0.2, 1.0 - abs(a.Distance) / falloff);
#    opColor = strokeImplicit(wave, widthThin, opColor);
#    opColor = strokeImplicit(a, widthThick, opColor);
#
#    return opColor;
#}
#
#vec4 drawLine(Implicit a, vec4 opColor) {
#    a.Color.a = 0.75;
#    return strokeImplicit(a, 2.0, opColor);
#}
#
#vec4 drawFill(Implicit a, vec4 opColor) {
#    if (a.Distance <= 0.0)
#        return mix(opColor, a.Color, a.Color.a);
#
#    return opColor;
#}
#
#void mainImage(out vec4 fragColor, in vec2 fragCoord) {
#    vec4 opColor = vec4(1.0);
#
#    float angle = (-0.5 + readFloat(2.)) * pi;
#    direction = vec2(cos(angle), sin(angle));
#    viz = int(readFloat(1.) * 5.);
#
#    vec2 p = (fragCoord - 0.5 * iResolution.xy); // * iResolution.xy;
#
#    if (iMouse.x > bounds.x + bounds.z + 20.0 || iMouse.y > bounds.y + bounds.w + 20.0)
#        mouse = iMouse.xy - 0.5 * iResolution.xy;
#
#    vec3 p3 = vec3(p, 0.0);
#
#    float padding = iResolution.x * (0.3 + cos(iTime) * 0.05);
#    float size = iResolution.x * 0.1 + sin(iTime) * 12.0;
#
#    Implicit a = RectangleUGFSDFCenterRotated(fragCoord, vec2(padding, iResolution.y / 2.0), size * 1.8, iTime * 0.1, vec4(1., 0., 0., 1));
# //   Implicit a = RectangleCenterRotated(fragCoord, vec2(padding, iResolution.y / 2.0), vec2(size * 1.8), iTime * 0.1, vec4(1., 0., 0., 1));
#    Implicit b = Circle(fragCoord, vec2(iResolution.x - padding, iResolution.y / 2.0), size, vec4(0., 0., 1., 1));
#
#    Implicit shapes = Min(a, b);
#    Implicit sum = Add(a, b);
#    Implicit diff = Subtract(a, b);
#    Implicit interp = Divide(diff, sum);
#
#    switch (viz) {
#    case 0:
#        opColor = drawImplicit(shapes, opColor);
#        break;
#    case 1:
#        opColor = drawImplicit(Multiply(sum, 0.5), opColor);
#        break;
#    case 2:
#        opColor = drawImplicit(Multiply(diff, 0.5), opColor);
#        break;
#    case 3:
#        opColor = min(
#            drawImplicit(Multiply(sum, 0.5), opColor),
#            drawImplicit(Multiply(diff, 0.5), opColor)
#        );
#        break;
#    default:
#        opColor = min(
#            drawImplicit(Multiply(interp, 100.), opColor),
#            drawImplicit(Multiply(Subtract(1., Abs(interp)), 100.), opColor)
#        );
#        break;
#    }
#
#    if (shapes.Distance < 0.)
#        opColor.rgb = min(opColor.rgb, opColor.rgb * 0.65 + shapes.Color.rgb * 0.2);
#
#    vec4 ui = texture(iChannel0, fragCoord.xy/iResolution.xy);
#    opColor = mix(opColor, ui, ui.a);
#
# //   opColor = DrawVectorField(p3, Divide(shape, length(shape.Gradient)), opColor, 25., 1.);
#
#    fragColor = opColor;
#}
#
#

def show_slice(*args, **kwargs):
    import matplotlib.pyplot as plt
    a, extent, axes = sample_slice(*args, **kwargs)
    amax = np.amax(a)
    amin = np.amin(a)
    amin = kwargs.pop('min', amin)
    amax = kwargs.pop('max', amax)
    print(extent, amin, amax)
    #a = a.reshape(-1)
    #a = np.where(a < 0, 
    #    np.outer( a/amin, np.array((.25,0,0,1)) ),
    #    np.outer( a/amax, np.array((0,0,.25,1)) ))
    #a = a.reshape(extent[0], extent[1])
    plt.figure(figsize=(extent[1]-extent[0], extent[3]-extent[2]))
    #plt.axis('equal')
    #im = plt.imshow(a, cmap="RdBu", extent=extent, origin='lower')
    im = plt.contour(a, levels=np.arange(-2, 2, 0.1), colors='black')
    im.axes.get_xaxis().set_visible(False)
    im.axes.get_yaxis().set_visible(False)
    #plt.set_aspect(extent[1]-extent[0], extent[3]-extent[2])
    #im.set_aspect('equal')
    #plt.xlabel(axes[0])
    #plt.ylabel(axes[1])
    #plt.colorbar(im)
    plt.show()

show_slice(sphere(), z=0, bounds=((-2,-2,-2),(2,2,2)))
