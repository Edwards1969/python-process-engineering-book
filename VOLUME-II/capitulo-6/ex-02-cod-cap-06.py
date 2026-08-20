# -*- coding: utf-8 -*-
"""

6.3 Tabela Inicial de Dados Térmicos. - pág. 341- 342

"""
import numpy as np
import pandas as pd

# Tempo de simulação
tempo = np.arange(0, 1800, 1)

# Temperatura real do processo (variação lenta + perturbação rápida)
T_real = 80 + 20*np.sin(0.002*tempo) + 2*np.sin(0.05*tempo)

# --- Termopar ---
S = 0.041
tau_tc = 12
T_tc = np.zeros_like(T_real)

for i in range(1, len(T_real)):
	T_tc[i] = T_tc[i-1] + (T_real[i] - T_tc[i-1]) / tau_tc

ruido_tc = np.random.normal(0, 0.2, len(T_real))
E_tc = S*T_tc + ruido_tc

# --- Pt100 ---
R0 = 100
a = 3.9083e-3
b = -5.775e-7
R_pt100 = R0*(1 + a*T_real + b*T_real**2)

# --- NTC ---
R0_ntc = 10000
T0 = 298.15
B = 3950
T_K = T_real + 273.15
R_ntc = R0_ntc * np.exp(B*(1/T_K - 1/T0))

# Tabela final
tabela_termica = pd.DataFrame({
	"tempo_s": tempo,
	"T_real_C": T_real,
	"T_termopar_C": T_tc,
	"Tensao_termopar_mV": E_tc,
	"R_Pt100_Ohm": R_pt100,
	"R_NTC_Ohm": R_ntc
})

# Salvando para uso posterior
tabela_termica.to_csv("dados_termicos_simulados.csv", index=False)
