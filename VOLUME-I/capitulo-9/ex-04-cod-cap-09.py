# -*- coding: utf-8 -*-
"""

9.4 Balanços de Massa e Energia como Base da Modelagem. pág. 262-263.

"""
import numpy as np
import matplotlib.pyplot as plt

# Vazões de entrada e saída
m_in = 5.0                     # entrada constante (kg/s)
t = np.linspace(0, 50, 500)    # tempo de simulação
m_out = 2.0 + 0.05 * t         # saída aumentando lentamente

# Discretização do balanço de massa
dt = t[1] - t[0]
M = np.zeros_like(t)
M[0] = 0.0                     # massa inicial

# Balanço: dM/dt = m_in - m_out
for k in range(1, len(t)):
	dMdt = m_in - m_out[k-1]
	M[k] = M[k-1] + dMdt * dt

# Gráfico
plt.plot(t, M)
plt.xlabel("Tempo (s)")
plt.ylabel("Massa acumulada (kg)")
plt.title("Balanço de massa: acumulação ao longo do tempo")
plt.grid()
plt.show()

