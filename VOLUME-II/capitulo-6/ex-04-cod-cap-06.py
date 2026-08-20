# -*- coding: utf-8 -*-
"""

6.5 Simulação de falha em Sensores Térmicos. - 346 - 347
6.5.1 Desvio de Calibração (Offset)

"""
import numpy as np
import pandas as pd

tempo = np.arange(0, 1800, 1)
T_real = 80 + 20*np.sin(0.002*tempo)

# Termopar saudável
S = 0.041
tau_tc = 12
T_tc = np.zeros_like(T_real)
for i in range(1, len(T_real)):
	T_tc[i] = T_tc[i-1] + (T_real[i] - T_tc[i-1]) / tau_tc

ruido_tc = np.random.normal(0, 0.2, len(T_real))
E_tc = S*T_tc + ruido_tc

# Falha por offset
offset = 5.0
T_tc_falho = T_tc + offset

tabela_falha_offset = pd.DataFrame({
	"tempo_s": tempo,
	"T_real_C": T_real,
	"T_termopar_C": T_tc,
	"T_termopar_falho_C": T_tc_falho
})

"""

6.5.2 Aumento do Ruído. - pág. 347

"""
ruido_normal = np.random.normal(0, 0.2, len(T_real))
ruido_excessivo = np.random.normal(0, 1.0, len(T_real))

T_ruidoso_normal = T_tc + ruido_normal
T_ruidoso_falho = T_tc + ruido_excessivo

tabela_falha_ruido = pd.DataFrame({
	"tempo_s": tempo,
	"T_termopar_normal_C": T_ruidoso_normal,
	"T_termopar_falho_C": T_ruidoso_falho
})

"""

6.5.3 Sinal Saturado.  -  pág.348

"""

Tmin = 50
Tmax = 120

T_saturado = np.clip(T_tc, Tmin, Tmax)

tabela_falha_saturacao = pd.DataFrame({
	"tempo_s": tempo,
	"T_termopar_C": T_tc,
	"T_termopar_saturado_C": T_saturado
})

"""

6.5.4 Sinal Congelado (Sensor Travado).  -  pág. 348

"""
Tmin = 50
Tmax = 120

T_saturado = np.clip(T_tc, Tmin, Tmax)

tabela_falha_saturacao = pd.DataFrame({
	"tempo_s": tempo,
	"T_termopar_C": T_tc,
	"T_termopar_saturado_C": T_saturado
})

"""

6.5.4 Sinal Congelado (Sensor Travado). -  pág. 348

"""
T_congelado = T_tc.copy()
t_falha = 900
T_congelado[t_falha:] = T_congelado[t_falha]
tabela_falha_congelado = pd.DataFrame({
	"tempo_s": tempo,
	"T_termopar_C": T_tc,
	"T_termopar_congelado_C": T_congelado
})

"""

6.5.5 Visualização das Falhas. - pág. 349

"""
import matplotlib.pyplot as plt

# Exemplo: offset
plt.figure(figsize=(10,5))

# Linha contínua preta
plt.plot(tempo, T_tc, color="black", linestyle="-", label="Sensor Saudável")

# Linha tracejada preta
plt.plot(tempo, T_tc_falho, color="black", linestyle="--", label="Sensor com Offset")

plt.xlabel("Tempo (s)")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)
plt.show()





























