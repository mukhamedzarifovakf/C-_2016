import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10,10.01,0.01)
for i in x:
    if i**2-i-6==0:
        print(i)
plt.plot(x,x**2-x-6)
plt.title(r'$f(x)$')
plt.show()