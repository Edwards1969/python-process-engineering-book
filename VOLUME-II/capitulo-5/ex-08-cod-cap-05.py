# -*- coding: utf-8 -*-
"""

Termistores. pág. 281

"""
import numpy as np 
import pandas as pd


# Faixa de temperatura (°C)
T_C = np.linspace(0, 100, 500)
T_K = T_C + 273.15

# Parâmetros
R0 = 10000
T0 = 298.15
B = 3950

# Modelo
R = R0*np.exp(B*(1/T_K - 1/T0))

# Sensibilidade
dR_dT = R*(-B/(T_K**2))

tabela_ntc = pd.DataFrame({
		"Temperatura_C": T_C,
		"Resistencia_ohm": R,
		"dR_dT": dR_dT
	})

tabela_ntc


