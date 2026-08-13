# -*- coding: utf-8 -*-
"""

Simulação da Dinâmica de um Transmissor. pág. 127

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parâmetros do transmissor
tau = 0.25   # constante de tempo (s)
dt = 0.01
tempo = np.arange(0, 5, dt)

# Degrau de pressão
P_in = np.zeros_like(tempo)

P_in[tempo >= 1] = 10   # degrau para 10 bar

# Resposta dinâmica
P_m = np.zeros_like(tempo)

for i in range(1, len(tempo)):
	P_m[i] = P_m[i-1] + (dt/tau)*(P_in[i] - P_m[i-1])

tabela_dinamica = pd.DataFrame({
	"tempo_s": tempo,
	"P_entrada_bar": P_in,
	"P_medida_bar": P_m
})

# Gráfico da Resposta Dinâmica
plt.figure(figsize=(8,5))
plt.plot(tempo, P_in, color="black", linestyle="--", label="Pressão Real")
plt.plot(tempo, P_m, color="black", linewidth=1.8, label="Pressão Medida")
plt.xlabel("Tempo (s)")
plt.ylabel("Pressão (bar)")
plt.title("Resposta Dinâmica de um Transmissor de Pressão")
plt.grid(True)
plt.legend()
plt.show()
