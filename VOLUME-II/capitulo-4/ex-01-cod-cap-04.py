# -*- coding: utf-8 -*-
"""

4.5 Cálculo de Vazão por Placa de Orifício com Python e pandas. - pág. 175

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leitura dos dados
tabela = pd.read_csv("dados_vazao_orificio.csv")

# Parâmetros do sistema
Cd = 0.61                 # coeficiente de descarga típico
D = 0.10                  # diâmetro da tubulação (m)
d = 0.05                  # diâmetro do orifício (m)
beta = d / D              # razão beta
A2 = np.pi * (d**2) / 4   # área da seção contraída

# Cálculo da vazão
tabela["Vazao_m3_s"] = (
	Cd * A2 * np.sqrt(
	(2 * tabela["DeltaP_Pa"]) /
	(tabela["Densidade_kg_m3"] * (1 - beta**4))
	)
	)

# Arredondamento para melhor apresentação
tabela["Vazao_m3_s"] = tabela["Vazao_m3_s"].round(6)
print(tabela)

# Gráfico da Vazão ao Longo do Tempo

plt.figure(figsize=(10,5))
plt.plot(tabela["Tempo_s"], tabela["Vazao_m3_s"], marker="o")
plt.xlabel("Tempo (s)")
plt.ylabel("Vazão (m³/s)")
plt.title("Variação da Vazão ao Longo do Tempo")
plt.grid(True)
plt.show()

