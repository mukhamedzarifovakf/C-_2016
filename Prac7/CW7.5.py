import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10, 10, 0.1)
plt.xkcd()
plt.plot(x, eval(input()))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()