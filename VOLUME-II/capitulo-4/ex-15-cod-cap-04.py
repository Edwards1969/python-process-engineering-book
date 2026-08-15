# -*- coding: utf-8 -*-
"""

4.18.1 - Modelo 1D: Desenvolvimento do Perfil de Velocidade em um Tubo

"""
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros físicos e numéricos
L = 1.0          # raio normalizado do tubo (m)
nx = 101         # número de pontos
dx = L / (nx-1)
dpdz = -100.0    # gradiente de pressão (Pa/m)
mu = 1.0         # viscosidade dinâmica (Pa·s)

# Malha radial
x = np.linspace(0, L, nx)

# Matriz de coeficientes (diferenças finitas)
A = np.zeros((nx, nx))
b = np.ones(nx) * (-dpdz / mu)

# Condições de contorno: u(0) simetria, u(L)=0 (parede)
A[0,0] = 1.0
b[0] = 0.0
A[-1,-1] = 1.0
b[-1] = 0.0

# Preenchendo a matriz interna
for i in range(1, nx-1):
	A[i, i-1] = 1.0 / dx**2
	A[i, i]   = -2.0 / dx**2
	A[i, i+1] = 1.0 / dx**2
    
# Solução do sistema linear
u = np.linalg.solve(A, b)

# Gráfico final
plt.figure(figsize=(8,4))
plt.plot(x, u, label="Velocidade axial")
plt.xlabel("Raio normalizado (m)")
plt.ylabel("Velocidade (m/s)")
plt.title("Perfil de velocidade laminar em um tubo (Poiseuille 1D)")
plt.grid(True)
plt.legend()
plt.show()
