# -*- coding: utf-8 -*-
"""

Simulação com Variação de Densidade. - pág. 150

"""
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Parametros do sistema (placa de orificio)
# ---------------------------------------------------------
rho = 850        # densidade nominal do fluido (kg/m3)
C = 0.62         # coeficiente de descarga tipico
D = 0.15         # diametro da tubulacao (m)
d = 0.075        # diametro do orificio (m)

# Area do orificio
A = np.pi * (d**2) / 4

# ---------------------------------------------------------
# Vazoes simuladas (m3/s)
# ---------------------------------------------------------

Q = np.linspace(0, 0.02, 200)
# ---------------------------------------------------------
# Calculo da pressao diferencial nominal
# Relacao fundamental:
#     Q = C * A * sqrt(2 * deltaP / rho)
# Isolando deltaP:
#     deltaP = (Q / (C * A))**2 * (rho / 2)
# ---------------------------------------------------------
DP_nominal = (Q / (C * A))**2 * (rho / 2)
# ---------------------------------------------------------

# Simulacao com variacao de densidade (+/- 10%)
# ---------------------------------------------------------
rho_variacoes = [0.9 * rho, rho, 1.1 * rho]
DP_var = {}
for r in rho_variacoes:
    DP_var[r] = (Q / (C * A))**2 * (r / 2)
# ---------------------------------------------------------
# Grafico comparativo
# ---------------------------------------------------------
plt.figure(figsize=(8,5))
plt.plot(Q, DP_var[0.9 * rho] / 1000,
color="black", linestyle="--", label="Densidade -10%")
plt.plot(Q, DP_var[rho] / 1000,
color="black", linewidth=1.8, label="Densidade nominal")
plt.plot(Q, DP_var[1.1 * rho] / 1000,
color="black", linestyle=":", label="Densidade +10%")
plt.xlabel("Vazao (m3/s)")
plt.ylabel("Pressao Diferencial (kPa)")
plt.title("Efeito da Densidade na Medicao por Pressao Diferencial")
plt.grid(True)
plt.legend()
plt.show()

