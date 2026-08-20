# -*- coding: utf-8 -*-
"""

6.2 Comparação entre Sensores e Temperatura. - pág. 339-340 

"""
import numpy as np
import pandas as pd

tempo = np.arange(0, 600, 1)
T_real = 60 + 15*np.sin(0.01*tempo)

# --- Termopar ---
S = 0.041
tau_tc = 10
T_tc = np.zeros_like(T_real)

for i in range(1, len(T_real)):
	T_tc[i] = T_tc[i-1] + \
	(T_real[i] - T_tc[i-1]) / tau_tc

ruido_tc = np.random.normal(0, 0.15, len(T_real))
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

tabela_comparacao = pd.DataFrame({
	"tempo_s": tempo,
	"T_real_C": T_real,
	"T_termopar_C": T_tc,
	"Tensao_termopar_mV": E_tc,
	"R_Pt100_Ohm": R_pt100,
	"R_NTC_Ohm": R_ntc
})

"""

6.2.5 Visualização Gráfica

""" 
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
plt.plot(tempo, T_real, label="Temperatura Real")
plt.plot(tempo, T_tc, label="Termopar (°C)")
plt.xlabel("Tempo (s)")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10,5))
plt.plot(tempo, R_pt100, label="Pt100 (Ohm)")
plt.plot(tempo, R_ntc, label="NTC (Ohm)")
plt.xlabel("Tempo (s)")
plt.ylabel("Resistência (Ohm)")
plt.legend()
plt.grid(True)
plt.show()














