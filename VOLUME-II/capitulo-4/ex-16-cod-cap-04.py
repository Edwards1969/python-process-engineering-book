# -*- coding: utf-8 -*-
"""

4.18.2 Modelo 2D: Escoamento Laminar em um Canal Retangular. pág. 237

"""
import numpy as np
import matplotlib.pyplot as plt

# Dimensões do canal
Lx, Ly = 1.0, 1.0
nx, ny = 51, 51
dx, dy = Lx/(nx-1), Ly/(ny-1)

# Propriedades do fluido e gradiente de pressão
mu = 1.0          # viscosidade dinâmica (Pa·s)
dpdz = -100.0     # gradiente de pressão (Pa/m)

# Malha
x = np.linspace(0, Lx, nx)
y = np.linspace(0, Ly, ny)

# Campo de velocidade
u = np.zeros((ny, nx))

# Matriz auxiliar
un = u.copy()

# Iterações (método iterativo de Gauss-Seidel)
nt = 2000

for n in range(nt):
	un[:, :] = u[:, :]
	for j in range(1, ny-1):
		for i in range(1, nx-1):
			u[j, i] = 0.25 * (
				un[j, i+1] + un[j, i-1] +
				un[j+1, i] + un[j-1, i] -
				dx*dy * (dpdz/mu)
				)
	# Condições de contorno: paredes → velocidade zero
	u[0, :] = 0.0
	u[-1, :] = 0.0
	u[:, 0] = 0.0
	u[:, -1] = 0.0

# Gráfico
plt.figure(figsize=(6,5))
X, Y = np.meshgrid(x, y)
cont = plt.contourf(X, Y, u, levels=20, cmap="jet")
plt.colorbar(cont, label="Velocidade (m/s)")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Escoamento laminar 2D em um canal retangular (Poiseuille)")
plt.tight_layout()
plt.show()

