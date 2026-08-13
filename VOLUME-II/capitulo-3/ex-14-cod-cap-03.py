# -*- coding: utf-8 -*-
"""

Projeto Computacional de Engenharia — Análise de Nível em Tanque Industrial
a partir de Dados Reais. - pág. 161

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Constantes físicas
rho = 1000      # densidade da água (kg/m3)
g = 9.81        # gravidade (m/s2)

# Leitura do arquivo CSV
dados = pd.read_csv("dados_tanque.csv")
tempo = dados["tempo_s"]
pressao = dados["pressao_Pa"]
vazao = dados["vazao_m3s"]

# Cálculo do nível do tanque
nivel = pressao / (rho * g)

# Estatísticas do nível
nivel_medio = np.mean(nivel)
nivel_max = np.max(nivel)
nivel_min = np.min(nivel)
nivel_std = np.std(nivel)

print("Nível médio =", nivel_medio, "m")
print("Nível máximo =", nivel_max, "m")
print("Nível mínimo =", nivel_min, "m")
print("Desvio padrão =", nivel_std)

# Gráfico Pressão x Tempo
plt.figure()
plt.plot(tempo, pressao, color='black', linewidth=1.6)
plt.xlabel("Tempo (s)")
plt.ylabel("Pressão (Pa)")
plt.title("Pressão medida no transmissor")
plt.grid(True)
plt.show()

# Gráfico Nível x Tempo
plt.figure()
plt.plot(tempo, nivel, color='black', linewidth=1.6)
plt.xlabel("Tempo (s)")
plt.ylabel("Nível (m)")
plt.title("Nível do tanque calculado")
plt.grid(True)
plt.show()

# Gráfico Vazão x Tempo
plt.figure()
plt.plot(tempo, vazao, color='black', linewidth=1.6)
plt.xlabel("Tempo (s)")
plt.ylabel("Vazão de entrada (m3/s)")
plt.title("Vazão de alimentação do tanque")
plt.grid(True)
plt.show()

