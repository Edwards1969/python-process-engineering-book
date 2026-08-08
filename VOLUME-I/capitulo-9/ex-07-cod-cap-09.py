# -*- coding: utf-8 -*-
"""

9.6 Modelagem de Tanques e Vasos Industriais. pág. 268-269.

"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parâmetros do tanque
A = 1.0        # área da seção transversal (m^2)
C = 0.6        # coeficiente de descarga (m^(3/2)/s)
q_in = 1.2     # vazão de entrada (m^3/s)

# Modelo dinâmico: dh/dt = (q_in - C*sqrt(h)) / A
def modelo(t, h):
	q_out = C * np.sqrt(max(h[0], 0))
	dhdt = (q_in - q_out) / A
	return [dhdt]

# Simulação
sol = solve_ivp(modelo, [0, 80], [0.1], max_step=0.1)

# Gráfico
plt.plot(sol.t, sol.y[0])
plt.xlabel("Tempo (s)")
plt.ylabel("Nível (m)")
plt.title("Dinâmica de um tanque com saída por gravidade")
plt.grid()
plt.show()	

