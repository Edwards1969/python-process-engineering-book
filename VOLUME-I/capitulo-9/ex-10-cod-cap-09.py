# -*- coding: utf-8 -*-
"""

9.9 Modelagem Dinâmica de Separadores Trifásicos. pág. 279-281

"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parâmetros do separador
V_total = 12.0
A = 2.0
R = 8.314
T = 350.0
Co = 0.7
Ca = 0.9

# Vazões de entrada
mg_in = 5.0
mo_in = 4.0
ma_in = 3.0

# Propriedades
MW_g = 0.020
rho_o = 850.0
rho_a = 1000.0

# Modelo dinâmico
def modelo(t, x):
	P, ho, ha = x
	Vg = V_total - A*(ho + ha)
	Mg = P*Vg/(R*T)*MW_g
	mg_out = 0.5 * P
	mo_out = Co * np.sqrt(max(ho, 0))
	ma_out = Ca * np.sqrt(max(ha, 0))
	dMgdt = mg_in - mg_out
	dModt = mo_in - mo_out
	dMadt = ma_in - ma_out
	dPdt = (R*T/MW_g)*(dMgdt/Vg + Mg*A/(Vg**2)*(dModt/rho_o + dMadt/rho_a))
	dhodt = dModt/(rho_o*A)
	dhadt = dMadt/(rho_a*A)
	return [dPdt, dhodt, dhadt]

# Simulação
sol = solve_ivp(modelo, [0, 200], [1e5, 0.4, 0.3], max_step=0.1)

# Gráficos
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.plot(sol.t, sol.y[0]/1e5)
plt.xlabel("Tempo (s)", fontsize=10)
plt.ylabel("Pressão (bar)", fontsize=10)
plt.grid()

plt.subplot(1,3,2)
plt.plot(sol.t, sol.y[1])
plt.xlabel("Tempo (s)", fontsize=10)
plt.ylabel("Nível de óleo (m)", fontsize=10)
plt.grid()

plt.subplot(1,3,3)
plt.plot(sol.t, sol.y[2])
plt.xlabel("Tempo (s)", fontsize=10)
plt.ylabel("Nível de água (m)", fontsize=10)
plt.grid()

plt.suptitle("Dinâmica simplificada de um separador trifásico", fontsize=12)

plt.tight_layout(rect=[0, 0, 1, 0.95])  # aumenta espaço para o título e margens
plt.show()

