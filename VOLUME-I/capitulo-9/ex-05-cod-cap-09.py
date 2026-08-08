# -*- coding: utf-8 -*-
"""

9.5 Modelos Dinâmicos de Primeira e Segunda Ordem. - pág. 265-266.

Modelo de primeira ordem.

"""
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do modelo de primeira ordem
K = 2.0       # ganho estático
tau = 12.0    # constante de tempo (s)
u = 1.0       # degrau de entrada
y0 = 0.0      # condição inicial

# Discretização temporal
dt = 0.1
t = np.arange(0, 80, dt)
y = np.zeros_like(t)
y[0] = y0

# Modelo: dy/dt = (K*u - y)/tau
for k in range(1, len(t)):
	dydt = (K*u - y[k-1]) / tau
	y[k] = y[k-1] + dydt * dt

# Gráfico
plt.plot(t, y)
plt.xlabel("Tempo (s)")
plt.ylabel("y(t)")
plt.title("Resposta a degrau de um sistema de primeira ordem")
plt.grid()
plt.show()


