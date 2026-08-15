# -*- coding: utf-8 -*-
"""

5.5.1 Modelo de Primeira Ordem a partir do Balanço de Energia. pág. 286

"""
import numpy as np
import pandas as pd

tempo = np.arange(0, 300, 1)
dt = 1
T_fonte = 120
T0 = 25
tau = 20
T = np.zeros_like(tempo, dtype=float)
T[0] = T0

for k in range(len(tempo)-1):
	T[k+1] = T[k] + (dt/tau)*(T_fonte - T[k])

tabela_aquecimento = pd.DataFrame({
		"tempo_s": tempo,
		"T_C": T
	})

"""

5.5.2 Identificação Experimental da Constante de Tempo. pág. 288

"""
T_inf = T_fonte
y = np.log(np.abs(T - T_inf + 1e-6))
coef = np.polyfit(tempo, y, 1)
tau_estimado = -1/coef[0]
tau_estimado

"""

5.5.3 Modelo com Perturbação Variável. pág. 288

"""
T_fonte_var = 120 + 15*np.sin(0.02*tempo)
T = np.zeros_like(tempo, dtype=float)
T[0] = 25
for k in range(len(tempo)-1):
	T[k+1] = T[k] + (dt/tau)*(T_fonte_var[k] - T[k])
tabela_perturbada = pd.DataFrame({
		"tempo_s": tempo,
		"T_fonte_C": T_fonte_var,
		"T_sistema_C": T
	})
tabela_perturbada

"""

5.5.4 Modelo de Resfriamento: Lei de Newton. pág.289

"""
tempo = np.arange(0, 400, 1)
T_amb = 25
T0 = 180
k = 0.015
T = T_amb + (T0 - T_amb)*np.exp(-k*tempo)
tabela_resfriamento = pd.DataFrame({
		"tempo_s": tempo,
		"T_C": T
	})
tabela_resfriamento

"""

5.5.5 Integração Planta + Sensor. pág. 291

"""
tau_sensor = 8
T_sensor = np.zeros_like(T)
for k in range(len(tempo)-1):
	T_sensor[k+1] = T_sensor[k] + (dt/tau_sensor)*(T[k] - T_sensor[k])
tabela_integrada = pd.DataFrame({
		"tempo_s": tempo,
		"T_planta_C": T,
		"T_sensor_C": T_sensor
	})

tabela_integrada

