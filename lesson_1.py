%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 201)

plt.plot(x, np.cos(x))
plt.plot(x, np.cos(3*x))
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-1.2,1.2) 
plt.grid(True)
