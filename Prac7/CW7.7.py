import numpy as np
import matplotlib.pyplot as plt

def y(x):
    A = 0
    a = 3
    b = 0.5
    n = 100
    for i in range(n):
        A += b**i*np.cos(a**i*np.pi*x)
    return A

x=np.arange(-2,2,0.0001)

plt.plot(x, y(x))
plt.show()