# -*- coding: utf-8 -*-
"""

9.2 Introdução à Modelagem Dinâmica. - pág. 256-258.

"""
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do forno
T_set = 200.0     # temperatura alvo (°C)
tau = 30.0        # constante de tempo (s)
T0 = 25.0         # temperatura inicial (°C)

# Discretização temporal
dt = 0.5
t = np.arange(0, 300, dt)
T = np.zeros_like(t)
T[0] = T0

# Modelo dinâmico: dT/dt = (T_set - T)/tau
for k in range(1, len(t)):
	dTdt = (T_set - T[k-1]) / tau
	T[k] = T[k-1] + dTdt * dt

# Gráfico
plt.plot(t, T)
plt.xlabel("Tempo (s)")
plt.ylabel("Temperatura (°C)")
plt.title("Aquecimento dinâmico de um forno elétrico")
plt.grid()
plt.show()	
    