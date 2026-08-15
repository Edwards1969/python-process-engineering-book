# -*- coding: utf-8 -*-
"""

5.3.1 Faixa Termométrica. pág. 258

"""
import numpy as np
import pandas as pd

# Tempo
dt = 1.0
tempo = np.arange(0, 800, dt)
# Processo real
T_real = 80 + 20*np.sin(0.02*tempo)

# -------------------------
# Sensor ideal
# -------------------------
T_ideal = T_real.copy()

# -------------------------
# Termopar tipo K
# -------------------------
tau_tc = 5
T_tc = np.zeros_like(T_real)
for i in range(1, len(T_real)):
	T_tc[i] = T_tc[i-1] + \
		(T_real[i] - T_tc[i-1]) / tau_tc
ruido_tc = np.random.normal(0, 0.5, len(T_real))
T_tc_medido = T_tc + ruido_tc

# -------------------------
# Pt100
# -------------------------
tau_pt = 12
T_pt = np.zeros_like(T_real)
for i in range(1, len(T_real)):
	T_pt[i] = T_pt[i-1] + \
		(T_real[i] - T_pt[i-1]) / tau_pt
ruido_pt = np.random.normal(0, 0.2, len(T_real))
T_pt_medido = T_pt + ruido_pt

# -------------------------
# Construção da tabela
# -------------------------
tabela = pd.DataFrame({
	"tempo_s": tempo,
	"T_real_C": T_real,
	"T_ideal_C": T_ideal,
	"T_termopar_C": T_tc_medido,
	"T_pt100_C": T_pt_medido
})

tabela

# -------------------------
# Cálculo do erro absoluto
# -------------------------
tabela["Erro_termopar"] = \
	abs(tabela["T_real_C"] - tabela["T_termopar_C"])
tabela["Erro_pt100"] = \
	abs(tabela["T_real_C"] - tabela["T_pt100_C"])
# Métricas
MAE_termopar = tabela["Erro_termopar"].mean()
MAE_pt100 = tabela["Erro_pt100"].mean()
print("MAE Termopar: {:.4f}".format(MAE_termopar))
print("MAE Pt100: {:.4f}".format(MAE_pt100))