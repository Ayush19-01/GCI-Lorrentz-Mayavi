#Made for the sole purpose of GCI 2019
import numpy
from mayavi import mlab
def equations(x,y,z):
    xpoint=10*(y - x)
    ypoint=28*x - y - x*z
    zpoint=x*y - 2.667*z
    return xpoint, ypoint, zpoint
x,y,z = numpy.mgrid[-50:50:100j, -50:50:100j, -10:60:70j]
xpoint,ypoint,zpoint = equations(x, y, z)
fig=mlab.figure(size=(500, 500), bgcolor=(0, 0, 0))
fill= mlab.flow(x, y, z, xpoint,ypoint,zpoint, line_width=3, colormap='Paired')
fill.module_manager.scalar_lut_manager.reverse_lut = True
fill.stream_tracer.integration_direction = 'both'
fill.stream_tracer.maximum_propagation = 200
src = fill.mlab_source.m_data
ext= mlab.pipeline.extract_vector_components(src)
ext.component = 'z-component'
zc = mlab.pipeline.iso_surface(ext, opacity=0.5, contours=[0, ],
            color=(0.6, 1, 0.4))
zc.actor.property.backface_culling = True
mlab.view(140, 120, 113, [0.65, 1.8, 30])
mlab.show()
