# -*- coding: utf-8 -*-
"""

9.10 Perturbações Operacionais e Análise do Comportamento Dinâmico. pág.281-284

"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parâmetros do separador
V_total = 10.0
A = 2.0
R = 8.314
T = 350.0
Cl = 0.8

# Vazões de entrada (antes e depois da perturbação)
mg_in = 5.0
ml_in_1 = 4.0
ml_in_2 = 7.0   # aumento repentino

# Propriedades
MW_g = 0.020
rho_l = 800.0

# Modelo dinâmico com perturbação
def modelo(t, x):
	P, h = x
	ml_in = ml_in_1 if t < 50 else ml_in_2
	Vg = V_total - A*h
	Mg = P*Vg/(R*T)*MW_g
	mg_out = 0.6 * P
	ml_out = Cl * np.sqrt(max(h, 0))
	dMgdt = mg_in - mg_out
	dMldt = ml_in - ml_out
	dPdt = (R*T/MW_g)*(dMgdt/Vg + Mg*A/(Vg**2)*dMldt/rho_l)
	dhdt = dMldt/(rho_l*A)
	return [dPdt, dhdt]

# Simulação
sol = solve_ivp(modelo, [0, 150], [1e5, 0.5], max_step=0.1)

# Gráficos
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.plot(sol.t, sol.y[0]/1e5)
plt.axvline(50, color='r', linestyle='--')
plt.xlabel("Tempo (s)")
plt.ylabel("Pressão (bar)")
plt.grid()

plt.subplot(1,2,2)
plt.plot(sol.t, sol.y[1])
plt.axvline(50, color='r', linestyle='--')
plt.xlabel("Tempo (s)")
plt.ylabel("Nível (m)")
plt.grid()

plt.suptitle("Resposta dinâmica a uma perturbação na vazão de entrada")
plt.show()

