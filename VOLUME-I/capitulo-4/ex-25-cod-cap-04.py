"""

4.5.5 Aplicação em Engenharia: distribuição de temperatura

"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)
T = 100 * np.exp(-0.1*(X**2 + Y**2))

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, T, cmap="inferno")
ax.set_title("Distribuição de Temperatura em uma Placa")

plt.show()
