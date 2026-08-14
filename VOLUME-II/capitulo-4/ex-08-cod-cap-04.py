# -*- coding: utf-8 -*-
"""

4.11 Relação Entre Vazão, Potência de Bombas e Custo Energético. - pág.200

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregamento dos dados
tabela = pd.read_csv("linha_agua.csv")

# Densidade da água em função da temperatura
tabela["Densidade_kg_m3"] = 1000 - 0.3 * (tabela["Temperatura_C"] - 20)

# Parâmetros físicos
g = 9.81
Cd = 0.61
D = 0.10   # diâmetro da tubulação (m)
d = 0.05   # diâmetro da garganta (m)
beta = d / D
A2 = np.pi * (d**2) / 4

# Altura manométrica obtida da pressão diferencial
tabela["H_m"] = tabela["DeltaP_Pa"] / (tabela["Densidade_kg_m3"] * g)

# Vazão pela placa de orifício
tabela["Vazao_m3_s"] = (
        Cd * A2 * np.sqrt(
        (2 * tabela["DeltaP_Pa"]) /
        (tabela["Densidade_kg_m3"] * (1 - beta**4))
        )
        )

# Potência hidráulica
tabela["Pot_hid_W"] = (
        tabela["Densidade_kg_m3"] * g *
        tabela["Vazao_m3_s"] * tabela["H_m"]
        )

# Potência elétrica
eta = 0.72
tabela["Pot_eletrica_W"] = tabela["Pot_hid_W"] / eta

# Custo Energético.
tarifa = 0.75  # R$/kWh
# Custo instantâneo (R$/s)
tabela["Custo_R_s"] = (
	tabela["Pot_eletrica_W"] * (1/3600) * tarifa
	)
	
# Custo acumulado
tabela["Custo_acumulado_R"] = tabela["Custo_R_s"].cumsum()

# Gráficos de Potência e Custo
plt.figure(figsize=(10,5))
plt.plot(tabela["Tempo_s"], tabela["Pot_eletrica_W"], color="purple")
plt.xlabel("Tempo (s)")
plt.ylabel("Potência (W)")
plt.title("Potência Elétrica Necessária ao Longo do Tempo")
plt.grid(True)
plt.show()

# Custo Energético Acumulado do Bombeamento
plt.figure(figsize=(10,5))
plt.plot(tabela["Tempo_s"], tabela["Custo_acumulado_R"], color="green")
plt.xlabel("Tempo (s)")
plt.ylabel("Custo (R$)")
plt.title("Custo Energético Acumulado do Bombeamento")
plt.grid(True)
plt.show()







