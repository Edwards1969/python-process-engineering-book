# -*- coding: utf-8 -*-
"""

9.8 Modelagem Dinâmica de Separadores Bifásicos. pág. 274-277.

"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parâmetros do separador
V_total = 10.0      # volume total (m^3)
A = 2.0             # área da seção transversal (m^2)
R = 8.314           # constante dos gases (J/mol.K)
T = 350.0           # temperatura (K)
Cl = 0.8            # coeficiente de descarga do líquido

# Vazões de entrada
mg_in = 5.0         # gás (kg/s)
ml_in = 4.0         # líquido (kg/s)

# Propriedades
MW_g = 0.020        # massa molar do gás (kg/mol)
rho_l = 800.0       # densidade do líquido (kg/m^3)

# Modelo dinâmico
def modelo(t, x):
	P, h = x
	Vg = V_total - A*h
	Mg = P*Vg / (R*T) * MW_g
	mg_out = 0.6 * P
	ml_out = Cl * np.sqrt(max(h, 0))
	dMgdt = mg_in - mg_out
	dMldt = ml_in - ml_out
	dPdt = (R*T/MW_g)*(dMgdt/Vg + Mg*A/(Vg**2)*dMldt/rho_l)
	dhdt = dMldt/(rho_l*A)
	return [dPdt, dhdt]

# Simulação
sol = solve_ivp(modelo, [0, 200], [1e5, 0.5], max_step=0.1)

# Gráficos
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(sol.t, sol.y[0]/1e5)
plt.xlabel("Tempo (s)")
plt.ylabel("Pressão (bar)")
plt.grid()

plt.subplot(1,2,2)
plt.plot(sol.t, sol.y[1])
plt.xlabel("Tempo (s)")
plt.ylabel("Nível (m)")
plt.grid()

plt.suptitle("Dinâmica simplificada de um separador bifásico")
plt.show()	

