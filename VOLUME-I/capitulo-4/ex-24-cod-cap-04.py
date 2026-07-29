"""

4.5.4 Mapas de contorno 3D.  -  pág. 87

"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Criando a malha X, Y
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)

X, Y = np.meshgrid(x, y)

# Definindo a superfície Z.
Z = np.sin(np.sqrt(X**2 + Y**2))

# Criando a figura 3D.
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Contorno 3D.
ax.contour3D(X, Y, Z, 50, cmap="plasma")
ax.set_title("Contorno 3D")

plt.show()