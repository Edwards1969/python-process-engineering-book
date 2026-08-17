# -*- coding: utf-8 -*-
"""

5.6 Simulação Computacional de Sensores Térmicos. pág. 

5.6.2 Exemplo Computacional: Termopar com Ruído, Atraso e Quantização 

"""
import numpy as np
import pandas as pd

tempo = np.arange(0, 600, 1)
# Temperatura real

T_real = 60 + 15*np.sin(0.01*tempo)
S = 0.041      # mV/°C
tau = 10
dt = 1
T_sensor = np.zeros_like(T_real)

for i in range(len(tempo)-1):
	T_sensor[i+1] = T_sensor[i] + (dt/tau)*(T_real[i] - T_sensor[i])
    
# Ruído térmico
ruido = np.random.normal(0, 0.15, len(tempo))

# Tensão ideal
E_mV = S*T_sensor + ruido

# Quantização A/D (12 bits, 0–100 mV)
resolucao = 100/4096

E_quant = np.round(E_mV/resolucao)*resolucao  # quant = quantized (quantizado)
tabela_termopar = pd.DataFrame({
		"tempo_s": tempo,
		"T_real_C": T_real,
		"T_sensor_C": T_sensor,
		"Tensao_mV": E_mV,
		"Tensao_quant_mV": E_quant
	})

tabela_termopar

# Exercício Avançado 1: Métricas Metrológicas - pág. 294

tabela_termopar["Erro_C"] = (
	tabela_termopar["T_real_C"] -
	tabela_termopar["T_sensor_C"]
	)
MAE = tabela_termopar["Erro_C"].abs().mean() # MAE — Mean Absolute Error
RMSE = np.sqrt((tabela_termopar["Erro_C"]**2).mean())  # RMSE — Root Mean Square Error
desvio_ruido = tabela_termopar["Tensao_mV"].std()

print("O Erro médio absoluto (MAE): {:.4f}".format(MAE))
print("O Erro Quadrático Médio (RMSE): {:.4f}".format(RMSE))
print("O desvio do ruido é: {:.4f}".format(desvio_ruido))

# Exercício Avançado 2: Filtragem Digital e Atraso. pág. 295
tabela_termopar["Tensao_filtrada"] = (
    tabela_termopar["Tensao_quant_mV"]
    .rolling(window=10)
    .mean()
)
tabela_termopar["Temp_filtrada_C"] = (
    tabela_termopar["Tensao_filtrada"]/S
)










