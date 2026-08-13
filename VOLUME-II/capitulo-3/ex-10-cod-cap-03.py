# -*- coding: utf-8 -*-
"""

3.7 Introdução à Vazão por Pressão Diferencial. - pág. 147 - 150

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#---------------------------------------------------------
# Parametros do sistema (placa de orificio)
#---------------------------------------------------------
rho = 850        # densidade do fluido (kg/m3)
C = 0.62         # coeficiente de descarga tipico
D = 0.15         # diametro da tubulacao (m)
d = 0.075        # diametro do orificio (m)

# Area do orificio
A = np.pi * (d**2) / 4

#---------------------------------------------------------
# Vazoes simuladas (m3/s)
#---------------------------------------------------------
Q = np.linspace(0, 0.02, 200)

#---------------------------------------------------------
# Calculo da pressao diferencial
# Relacao fundamental:
#     Q = C * A * sqrt(2 * deltaP / rho)
# Isolando deltaP:
#     deltaP = (Q / (C * A))**2 * (rho / 2)
#---------------------------------------------------------
DP = (Q / (C * A))**2 * (rho / 2)
# ---------------------------------------------------------

# Tabela de calibracao
#---------------------------------------------------------
tabela_dp = pd.DataFrame({
	"vazao_m3s": Q,
	"DP_Pa": DP,
	"DP_kPa": DP / 1000
})
print(tabela_dp.head())

#---------------------------------------------------------
# Grafico Vazao x Pressao Diferencial
#---------------------------------------------------------
plt.figure(figsize=(8,5))
plt.plot(Q, DP/1000, color="black", linewidth=1.8)
plt.xlabel("Vazão (m3/s)")
plt.ylabel("Pressão Diferencial (kPa)")
plt.title("Relação Vazão x Pressão Diferencial para Placa de Orifício")
plt.grid(True)
plt.show()
