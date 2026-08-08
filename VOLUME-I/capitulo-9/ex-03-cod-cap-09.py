# -*- coding: utf-8 -*-
"""

9.3 Fundamentos da Modelagem Dinâmica - pág. 259-261.

"""
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sistema de primeira ordem
u = 10.0      # valor imposto ao sistema
tau = 15.0    # constante de tempo (s)
x0 = 0.0      # condição inicial

# Discretização temporal
dt = 0.2
t = np.arange(0, 120, dt)
x = np.zeros_like(t)
x[0] = x0

# Modelo dinâmico: dx/dt = (u - x)/tau
for k in range(1, len(t)):
    dxdt = (u - x[k-1]) / tau
    x[k] = x[k-1] + dxdt * dt

# Gráfico
plt.plot(t, x)
plt.xlabel("Tempo (s)")
plt.ylabel("x(t)")
plt.title("Resposta dinâmica de um sistema de primeira ordem")
plt.grid()
plt.show()	
