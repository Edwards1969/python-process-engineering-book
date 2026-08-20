# -*- coding: utf-8 -*-
"""

6.4 Modelagem de Câmara Térmica e Reatores. - 343 

"""
import numpy as np
import pandas as pd

dt = 1.0
tempo = np.arange(0, 2000, dt)

# Parâmetros da câmara térmica
Tmax = 200
tau_c = 60
T = np.zeros_like(tempo, dtype=float)
T[0] = 25

# Ação de controle fixa (exemplo)
u = 0.5

# Perturbação externa
A = 1.5
omega = 0.01
d = A*np.sin(omega*tempo)

for i in range(1, len(tempo)):
	T_fonte = Tmax * u
	T[i] = T[i-1] + (T_fonte - T[i-1]) * dt / tau_c + d[i]

tabela_camara = pd.DataFrame({
	"tempo_s": tempo,
	"T_C": T,
	"perturbacao": d
})

"""

6.4.3 Modelo de Reator Químico. - 344 - 345

"""
# Parâmetros do reator

tau_r = 90
Tj = 120
T = np.zeros_like(tempo, dtype=float)
T[0] = 25
# Parâmetros da reação
k0 = 0.001
Ea = 45000
R = 8.314
dH = 50000
rhoCp = 4200

for i in range(1, len(tempo)):
	r = k0 * np.exp(-Ea/(R*(T[i-1] + 273.15)))
	termo_reacao = (dH / rhoCp) * r
	T[i] = T[i-1] + (Tj - T[i-1]) * dt / tau_r + termo_reacao

tabela_reator = pd.DataFrame({
	"tempo_s": tempo,
	"T_C": T
})