# -*- coding: utf-8 -*-
"""

4.12 Vazão de Fluidos Viscosos e Correções para Regime Laminar. - pág. 205

"""
import pandas as pd
import numpy as np

# Leitura dos dados
tabela = pd.read_csv("dados_fluidos_viscosos.csv")

# Parâmetros do sistema
Cd0 = 0.61
k = 15
D = 0.10
d = 0.05
beta = d / D
A2 = np.pi * (d**2) / 4

# Cálculo da velocidade aproximada (rho = densidade)
tabela["Velocidade_m_s"] = np.sqrt(
    2 * tabela["DeltaP_Pa"] / tabela["Densidade_kg_m3"]
)

# Número de Reynolds
tabela["Re"] = (
    tabela["Densidade_kg_m3"] *
    tabela["Velocidade_m_s"] *
    D /
    tabela["Viscosidade_Pa_s"]
)

# Coeficiente de descarga corrigido
tabela["Cd_corrigido"] = Cd0 * (1 + k / np.sqrt(tabela["Re"]))

# Cálculo da vazão corrigida
tabela["Vazao_corrigida_m3_s"] = (
    tabela["Cd_corrigido"] * A2 *
    np.sqrt(
        (2 * tabela["DeltaP_Pa"]) /
        (tabela["Densidade_kg_m3"] * (1 - beta**4))
    )
)

print(tabela)

# Gráfico da Vazão Corrigida

import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.plot(tabela["Re"], tabela["Vazao_corrigida_m3_s"],
marker="o", linestyle="--")
plt.xlabel("Número de Reynolds")
plt.ylabel("Vazão Corrigida (m³/s)")
plt.title("Correção da Vazão para Fluidos Viscosos")
plt.grid(True)
plt.show()