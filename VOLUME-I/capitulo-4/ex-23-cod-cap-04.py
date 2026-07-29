"""

4.5.3 Mapa de calor 3D (wireframe).  -  pág. 85

"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Criando a malha.
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

# Figura com dois gráficos lado a lado.
fig = plt.figure(figsize=(12,5))

# ----- Wireframe -----
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.plot_wireframe(X, Y, Z, color='black')
ax1.set_title('Wireframe (sem mapa de calor)')

#--- Superfície com colormap ----
ax2 = fig.add_subplot(1, 2, 2, projection="3d")
ax2.plot_surface(X, Y, Z, cmap="viridis")
ax2.set_title("Superfície com mapa de calor")

plt.show()