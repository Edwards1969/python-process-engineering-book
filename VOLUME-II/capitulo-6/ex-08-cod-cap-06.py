# -*- coding: utf-8 -*-
"""

6.6 Filtragem Digital de Sinais de Temperatura. - pág.350

"""
import numpy as np
import pandas as pd

# Sinal ruidoso (exemplo)
tempo = np.arange(0, 1800, 1)
T_real = 80 + 20*np.sin(0.002*tempo)
ruido = np.random.normal(0, 0.6, len(tempo))
T_ruidoso = T_real + ruido

# Média móvel
N = 15
T_mm = np.convolve(T_ruidoso, np.ones(N)/N, mode="same")

tabela_filtro_mm = pd.DataFrame({
	"tempo_s": tempo,
	"T_real_C": T_real,
	"T_ruidoso_C": T_ruidoso,
	"T_media_movel_C": T_mm
})


"""

6.6.2 Filtro Butterworth. pág. 351

"""
from scipy.signal import butter, filtfilt

fs = 1.0          # frequência de amostragem (Hz)
fc = 0.02         # frequência de corte (Hz)
ordem = 3

# Projeto do filtro Butterworth
b, a = butter(ordem, fc/(fs/2), btype="low")

# Aplicação com filtfilt (sem atraso de fase)
T_butter = filtfilt(b, a, T_ruidoso)

tabela_filtro_butter = pd.DataFrame({
	"tempo_s": tempo,
	"T_real_C": T_real,
	"T_ruidoso_C": T_ruidoso,
	"T_butter_C": T_butter
})

"""

6.9.3 Filtro de Kalman (Modelo Simples). - pág.352

"""
# Sinal medido (ruidoso)
z = T_ruidoso

# Inicialização
x_est = np.zeros_like(z)
P = np.zeros_like(z)

x_est[0] = z[0]
P[0] = 1.0

Q = 0.05   # variância do ruído de processo
R = 0.6    # variância do ruído de medição

for k in range(1, len(z)):
	# Predição
	x_pred = x_est[k-1]
	P_pred = P[k-1] + Q
    
	# Ganho de Kalman
	K = P_pred / (P_pred + R)
    
	# Atualização
	x_est[k] = x_pred + K*(z[k] - x_pred)
	P[k] = (1 - K)*P_pred

T_kalman = x_est

tabela_filtro_kalman = pd.DataFrame({
	"tempo_s": tempo,
	"T_real_C": T_real,
	"T_ruidoso_C": T_ruidoso,
	"T_kalman_C": T_kalman
})

"""

6.6.4 Comparação entre os Métodos de Filtragem. pág. 353

"""
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.plot(tempo, T_real, label="Temperatura Real")
plt.plot(tempo, T_ruidoso, label="Medida Ruidosa", alpha=0.4)
plt.plot(tempo, T_mm, label="Média Móvel")
plt.plot(tempo, T_butter, label="Butterworth")
plt.plot(tempo, T_kalman, label="Kalman")
plt.xlabel("Tempo (s)")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)
plt.show()

































