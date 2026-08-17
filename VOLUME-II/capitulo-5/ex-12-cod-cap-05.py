# -*- coding: utf-8 -*-
"""

5.6.3 Simulação de Sensores Pt100. pág. 296 -267

"""
import numpy as np
import pandas as pd

tempo = np.arange(0, 600, 1)  # arange = organizar

# Temperatura real
T_real = 60 + 15 * np.sin(0.01 * tempo)
R0 = 100
a = 3.90833e-3
b = -5.775e-7
R = R0 * (1 - a * T_real + b * T_real**2)

ruido_R = np.random.normal(0, 0.05, len(R))    
R_medido = R + ruido_R

tabela_pt100 = pd.DataFrame({
	"tempo_s": tempo,
	"T_real_C": T_real,
	"Resistencia_Ohm": R_medido
})

tabela_pt100 

# Exercício Avançado 3: Inversão Numérica.
A = b*R0
B = a*R0
C = R0 - tabela_pt100["Resistencia_Ohm"]
T_estimado = (-B + np.sqrt(B**2 - 4*A*C)) / (2*A)
tabela_pt100["T_estimado_C"] = T_estimado
tabela_pt100["Erro_C"] = (tabela_pt100["T_real_C"] - tabela_pt100["T_estimado_C"])








