

##### Графики на плоскости

### --- 1 Задание пункт: 

%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2*np.pi, 3*np.pi, 201)
plt.plot(x,  5*np.cos(x + 1) + 5)
plt.plot(x, -0.5*np.cos(x + 6))
plt.plot(x, 4*np.cos(x - 2)-5)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

### --- 3 Задание ---

## Напишите код, который будет переводить полярные координаты в декартовы.
a = np.linspace(0, 2*np.pi, 100)
r = 2
x = r*np.cos(a)
y = r*np.sin(a)
plt.plot(x, y)

## Напишите код, который будет рисовать график окружности в полярных координатах.
x = np.linspace(0, 2*np.pi, 100)
y = 4+0*np.cos(x)
plt.polar(x, y)

## Напишите код, который будет рисовать график отрезка прямой линии в полярных координатах.
#--- не сделано


### --- 4 Задание ---
## 1

from scipy.optimize import fsolve

def equations(p):
    x, y = p
    return (y - x**2 + 1, np.exp(x) + x - x*y - 1)

x1, y1 =  fsolve(equations, (-2, 3))
              
print (x1, y1)
x2, y2 =  fsolve(equations, (2, 3))
              
print (x2, y2)

## 2
#--- не сделано