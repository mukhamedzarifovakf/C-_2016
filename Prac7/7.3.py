import numpy as np
import matplotlib.pyplot as plt
def y(x):
    y = np.log((x ** 2 + 1) * np.exp(-abs(x) / 10), 1 + 1 / np.tan(1/(1 + np.sin(x) ** 2)))
x = np.arange(10, 10.01, 0.1)
plt.plot(x, y(x), lw = 3)
plt.show()