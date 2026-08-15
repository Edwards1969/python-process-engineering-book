# -*- coding: utf-8 -*-
"""

5.4 Sensores de Temperatura: Uma Visão Computacional. pág. 271

"""
import numpy as np
import pandas as pd

# Passo de tempo (s)
dt = 1

# Vetor de tempo
tempo = np.arange(0, 600, dt)

# Temperatura real do processo
T_real = 50 + 10*np.sin(0.01*tempo)

# Parâmetros do sensor
S = 0.041      # mV/°C
tau = 8        # constante de tempo (s)

# Inicialização
T_sensor = np.zeros_like(T_real)

# Modelo dinâmico discreto
for k in range(1, len(tempo)):
	T_sensor[k] = T_sensor[k-1] + \
	(dt/tau)*(T_real[k-1] - T_sensor[k-1])
    
	# Ruído térmico (°C)
	ruido = np.random.normal(0, 0.2, len(tempo))
    
# Conversão para tensão
E_mV = S*T_sensor + ruido

# DataFrame
tabela = pd.DataFrame({
		"tempo_s": tempo,
		"T_real_C": T_real,
		"T_sensor_C": T_sensor,
		"Tensao_mV": E_mV
	})

tabela

# 5.4.3 Exercício Avançado — Identificação e Filtragem. - pág.274

# Erro dinâmico
tabela["erro_C"] = tabela["T_real_C"] - tabela["T_sensor_C"]
# Erro médio absoluto
MAE = np.mean(np.abs(tabela["erro_C"]))
# Filtro de média móvel
tabela["Tensao_filtrada"] = \
tabela["Tensao_mV"].rolling(window=10).mean()





