import math
import pylab
from matplotlib import mlab

a = 1

tmin = -20.0
tmax = 20.0

dt = 0.01
tlist = mlab.frange (tmin, tmax, dt)

pylab.ion()

for n in range(250):
        xlist = [math.sin(t+a) for t in tlist]
        ylist = [math.cos(2*t) for t in tlist]
        pylab.clf()
        pylab.plot (xlist, ylist)
        pylab.draw()
        a += 0.05

pylab.close()