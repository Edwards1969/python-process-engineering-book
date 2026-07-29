"""

4.5.2 Superfície 3D.  -  pág.85

"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

x =  np.linspace(-5, 5, 50)
y =  np.linspace(-5, 5, 50)

X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('Superfície Parabólica')
plt.show()