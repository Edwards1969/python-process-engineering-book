# -*- coding: utf-8 -*-
"""

Cálculo da Densidade da Água. - pág. 197

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tabela = pd.read_csv("linha_agua.csv")

# Cálculo da densidade da água
tabela["Densidade_kg_m3"] = 1000 - 0.3 * (tabela["Temperatura_C"] - 20)

# Parâmetros do sistema.
Cd = 0.61   # coeficiente de descarga típico
D = 0.10    # diâmetro da tubulação (m)
d = 0.05    # diâmetro do orifício (m)
beta = d / D  # razão beta
A2 = np.pi * (d**2) / 4  # área da seção contraída

tabela["Vazao_m3_s"] = (
		Cd * A2 * np.sqrt(
		(2 * tabela["DeltaP_Pa"]) /
		(tabela["Densidade_kg_m3"] * (1 - beta**4))
		)
	)

# Gráfico da Vazão ao Longo do Tempo.
plt.figure(figsize=(10,5))
plt.plot(tabela["Tempo_s"], tabela["Vazao_m3_s"], color="blue")
plt.xlabel("Tempo (s)")
plt.ylabel("Vazão (m³/s)")
plt.title("Variação da Vazão na Linha de Água")
plt.grid(True)
plt.show()

# Cálculo do Volume Total Escoado.
tabela["Volume_m3"] = np.cumsum(
	tabela["Vazao_m3_s"] * tabela["Tempo_s"].diff().fillna(0)
	)
volume_total = tabela["Volume_m3"].iloc[-1]
print("Volume total escoado (m³):", volume_total)

# Detecção de Anomalias.
media = tabela["Vazao_m3_s"].mean()
desvio = tabela["Vazao_m3_s"].std()
lim_sup = media + 3 * desvio
lim_inf = media - 3 * desvio
tabela["Anomalia"] = (
	(tabela["Vazao_m3_s"] > lim_sup) |
	(tabela["Vazao_m3_s"] < lim_inf)
	)

print(tabela)














