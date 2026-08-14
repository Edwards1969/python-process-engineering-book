# -*- coding: utf-8 -*-
"""

Análise de Dados Reais de Vazão com pandas - pág. 184

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
    
tabela = pd.read_csv("vazao_industrial.csv")
print(tabela.head())

# Cálculo da Vazão a Partir da Pressão Diferencial
Cd = 0.61                # coeficiente de descarga típico
D = 0.10                 # diâmetro da tubulação (m)
d = 0.05			 	 # diâmetro do orifício (m)
beta = d / D             #  razão beta
A2 = np.pi * (d**2) / 4  # área da seção contraída
	
tabela["Vazao_m3_s"] = (
        Cd * A2 * np.sqrt(2 * tabela["DeltaP_Pa"]) /
        (tabela["Densidade_kg_m3"] *(1 - beta**4))
        )

tabela # caso você queira que apareça no console.
	
tabela["Vazao_m3_s"] = tabela["Vazao_m3_s"].round(6)

# Gráfico da Vazão ao Longo do Tempo
plt.figure(figsize=(10,5))
plt.plot(tabela["Tempo_s"], tabela["Vazao_m3_s"], color="blue")
plt.xlabel("Tempo (s)")
plt.ylabel("Vazão (m³/s)")
plt.title("Variação da Vazão ao Longo do Tempo")
plt.grid(True)
plt.show()

# Volume Acumulado.
tabela["Volume_m3"] = np.cumsum(
	tabela["Vazao_m3_s"] * (tabela["Tempo_s"].diff().fillna(0))
	)


plt.figure(figsize=(10,5))
plt.plot(tabela["Tempo_s"], tabela["Volume_m3"], color="red")
plt.xlabel("Tempo (s)")
plt.ylabel("Volume (m³)")
plt.title("Volume Acumulado ao Longo do Tempo")
plt.grid(True)
plt.show()


