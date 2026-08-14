# -*- coding: utf-8 -*-
"""

4.15 Estudo de Caso: Vazão de Petróleo em Plataforma Offshore. - pág. 217-220

"""
import pandas as pd

tabela = pd.read_csv("petroleo_offshore.csv")
print(tabela.head())

# Erro relativo entre instrumentos
tabela["Erro_relativo"] = (
(tabela["Coriolis_m3_s"] - tabela["Orificio_m3_s"]) /
	tabela["Coriolis_m3_s"]
	)

# Gráfico da Vazão.
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

# Linha Coriolis (preta, contínua)
plt.plot(
    tabela["Tempo_s"],
    tabela["Coriolis_m3_s"],
    label="Coriolis",
    linewidth=2,
    color="black",
    linestyle="-"
)

# Linha Placa de Orifício (preta, tracejada)
plt.plot(
    tabela["Tempo_s"],
    tabela["Orificio_m3_s"],
    label="Placa de Orifício",
    linewidth=2,
    color="black",
    linestyle="--",
    alpha=0.8
)

plt.xlabel("Tempo (s)")
plt.ylabel("Vazão (m³/s)")
plt.title("Vazão de Petróleo em Plataforma Offshore")
plt.grid(True)
plt.legend()
plt.show()

# Volume Total Produzido.
tabela["Volume_Coriolis"] = tabela["Coriolis_m3_s"].cumsum()
tabela["Volume_Orificio"] = tabela["Orificio_m3_s"].cumsum()
volume_coriolis = tabela["Volume_Coriolis"].iloc[-1]
volume_orificio = tabela["Volume_Orificio"].iloc[-1]
print("Volume medido pelo Coriolis: {:.2f}".format(volume_coriolis))
print("Volume medido pela Placa de Orifício: {:.2f}".format(volume_orificio))












