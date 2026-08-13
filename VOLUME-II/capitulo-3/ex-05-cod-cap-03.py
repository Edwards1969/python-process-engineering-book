# -*- coding: utf-8 -*-
"""

Simulação com Ruído de Medição. - pág. 132

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parâmetros do sensor
tau = 0.3
dt = 0.01 
tempo = np.arange(0, 5, dt)

# Pressão real: degrau aplicado em t = 1s
P_real = np.zeros_like(tempo) # degrau para 8 bar
P_real[tempo >=1] = 8.0 # degrau para 8 bar

# Respostao dinâmica do sensor.
P_medida = np.zeros_like(tempo)
for i in range(1, len(tempo)):
    P_medida[i] = P_medida[i-1] + (dt/tau)*(P_real[i]-P_medida[i-1])

tabela_dinamica_sensor = pd.DataFrame({
	"tempo_s": tempo,
	"P-real_bar": P_real,
	"P-medida_bar": P_medida
})

# Ruído gaussiano
ruido = np.random.normal(0, 0.05, len(tempo))  # 0.05 bar de desvio padrão
P_ruidosa = P_medida + ruido
tabela_ruido = pd.DataFrame({
	"tempo_s": tempo,
	"P_medida_bar": P_medida,
	"P_ruidosa_bar": P_ruidosa
})
plt.figure(figsize=(8,5))
plt.plot(tempo, P_medida, color="black", linewidth=1.8, label="Pressão Filtrada pelo Sensor")
plt.plot(tempo, P_ruidosa, color="black", linestyle=":", label="Pressão com Ruído")
plt.xlabel("Tempo (s)")
plt.ylabel("Pressão (bar)")
plt.title("Efeito do Ruído de Medição em Sensores de Pressão")
plt.grid(True)
plt.legend()
plt.show()
