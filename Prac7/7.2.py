import numpy as np
import matplotlib.pyplot as plt
def y(x):
    y = x*x-6-x
    return y
x = np.arange(-10, 10.01, 0.1)
plt.plot(x, y(x), x, 0*x, lw = 1)
plt.xlabel(r'$x$')
plt.ylabel(r'$y(x)$')
plt.show()