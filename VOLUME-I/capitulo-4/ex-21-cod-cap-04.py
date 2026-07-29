"""

4.5.1 Curvas tridimensionais.  -  pág. 84

"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, 500)

x = np.cos(t)
y = np.sin(t)
z = t

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z)
ax.set_title('Curva Helicoidal')
plt.show()