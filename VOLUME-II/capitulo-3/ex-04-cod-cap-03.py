# -*- coding: utf-8 -*-
"""

3.4 Dinâmica de Sensores de Pressão. pág. 129

"""
import numpy as np
import pandas as pd

# Parâmetros do sensor
tau = 0.3
dt = 0.01
tempo = np.arange(0, 5, dt)

# Pressão real: degrau aplicado em t = 1 s
P_real = np.zeros_like(tempo)

P_real[tempo >= 1] = 8.0   # degrau para 8 bar

# Resposta dinâmica do sensor
P_medida = np.zeros_like(tempo)

for i in range(1, len(tempo)):
	P_medida[i] = P_medida[i-1] + (dt/tau)*(P_real[i] - P_medida[i-1])
tabela_dinamica_sensor = pd.DataFrame({
	"tempo_s": tempo,
	"P_real_bar": P_real,
	"P_medida_bar": P_medida
})

# Gráfico da Resposta Dinâmica.
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))
plt.plot(tempo, P_real, color="black", linestyle="--", label="Pressão Real")
plt.plot(tempo, P_medida, color="black", linewidth=1.8, label="Pressão Medida")
plt.xlabel("Tempo (s)")
plt.ylabel("Pressão (bar)")
plt.title("Resposta Dinâmica de um Sensor de Pressão (Modelo de 1ª Ordem)")
plt.grid(True)
plt.legend()
plt.show()







