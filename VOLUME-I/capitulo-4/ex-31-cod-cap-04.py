"""

4.6.6 Mapa de contorno de pressão.  -  pág. 94-95

"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4*np.pi, 200)
y = np.linspace(0, 4*np.pi, 200)

X, Y = np.meshgrid(x, y)
P = 50 + 10*np.sin(X) * np.cos(Y)

plt.figure(figsize=(8,5), facecolor='white')
cont = plt.contourf(X, Y, P, levels=30, cmap='viridis')
plt.title('Mapa de Contorno de Pressão')
plt.xlabel('x')
plt.ylabel('y')

cbar = plt.colorbar(cont)
cbar.set_label('Presão (kPa)')

plt.show()