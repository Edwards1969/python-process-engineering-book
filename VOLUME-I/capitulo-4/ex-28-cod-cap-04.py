"""

4.6.3 Distribuição de temperatuar em uma placa.  -  pág. 92

"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)
T = 80 * np.exp(-0.1*(X**2 + Y**2))

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, T, cmap="inferno")
ax.set_title("Distribuição de Temperatura em uma Placa")

plt.show()