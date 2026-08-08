# -*- coding: utf-8 -*-
"""

9.5 Modelos Dinâmicos de Primeira e Segunda Ordem. - pág. 267-268.

Modelo de segunda ordem.

"""
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do modelo de segunda ordem
K = 1.0          # ganho estático
wn = 0.5         # frequência natural (rad/s)
zeta = 0.2       # fator de amortecimento
u = 1.0          # degrau de entrada

# Discretização temporal
dt = 0.1
t = np.arange(0, 80, dt)
y = np.zeros_like(t)
dy = np.zeros_like(t)

# Modelo de segunda ordem:
# d2y/dt2 = wn^2*(K*u - y) - 2*zeta*wn*dy/dt
for k in range(1, len(t)):
	d2ydt2 = wn**2 * (K*u - y[k-1]) - 2*zeta*wn * dy[k-1]
	dy[k] = dy[k-1] + d2ydt2 * dt
	y[k] = y[k-1] + dy[k] * dt

# Gráfico
plt.plot(t, y)
plt.xlabel("Tempo (s)")
plt.ylabel("y(t)")
plt.title("Resposta a degrau de um sistema de segunda ordem subamortecido")
plt.grid()
plt.show()	

