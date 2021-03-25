

##### Введение в аналитическую геометрию

### --- 1 Задание пункт 2: 

x = [10, 10, 10]
a = [0, 0, -10]
def vectorLength(x):
    sum = 0
    for a in x:
        sum += a**2
    
    print(sum)
    
    print(sum**.5)

vectorLength(x)

vectorLength(a)


### 3 задание 

%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import math
### Окружность
x = np.linspace(0, 6, 201)

y1 = []
y2 = []
for i in x:
    
    y1.append(math.sqrt(9-(i-3)**2))
    y2.append(-math.sqrt(9-(i-3)**2))

plt.plot(x, y1)
plt.plot(x, y2)
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

### эллипс
### Эллипс1

x = np.linspace(0, 12, 201)

a = 6
b = 1
y1 = []
y2 = []
for i in x:
    t = ((a**2)*(b**2)-(b**2)*((i-6)**2))/(a**2)
    y1.append(math.sqrt(t))
    y2.append(-math.sqrt(t))

plt.plot(x, y1)
plt.plot(x, y2)
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

### Эллипс2
x = np.linspace(0, 6, 201)

a = 6
b = 1
y1 = []
y2 = []
for i in x:
    y1.append(3*math.sqrt(9-(i-3)**2))
    y2.append(-3*math.sqrt(9-(i-3)**2))

plt.plot(x, y1)
plt.plot(x, y2)
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)


### Гипербола
x1 = np.linspace(0, 4, 201)
x2 = np.linspace(8, 12, 201)

a = 2
b = 1
y1 = []
y2 = []
y3 = []
y4 = []
for i in x1:
    t = ((b**2)*((i-6)**2)-(a**2)*(b**2))/(a**2)
    y1.append(math.sqrt(t))
    y2.append(-math.sqrt(t))

for i in x2:
    t = ((b**2)*((i-6)**2)-(a**2)*(b**2))/(a**2)
    y3.append(math.sqrt(t))
    y4.append(-math.sqrt(t))
    
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x2, y3)
plt.plot(x2, y4)
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)


#### Задание 5
## Нарисуйте трехмерный график двух параллельных плоскостей.
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 1)
Y = np.arange(-5, 5, 1)
print(X)
X, Y = np.meshgrid(X, Y)
print(Y)
print(X[1,1])
Z1 = 2*(X-3) + 3*(Y)+30
Z2 = 2*X + 3*Y
print(Z1)
print(Z2)
ax.plot_surface(X, Y, Z2)
ax.plot_surface(X, Y, Z1)
show()

#### Нарисуйте трехмерный график двух любых поверхностей второго порядка.

fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
print(X)
X, Y = np.meshgrid(X, Y)

Z1 = 2*(X**2) + 3*(Y**2)
Z2 = 2*(X**2) - 3*(Y**2)
# Z2 = 2*X + 3*Y

ax.plot_surface(X, Y, Z2)
ax.plot_surface(X, Y, Z1)
show()