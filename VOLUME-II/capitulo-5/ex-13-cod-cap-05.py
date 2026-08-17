# -*- coding: utf-8 -*-
"""

5.6.3 Simulação de Sensores Pt100. - pág. 296 - 298.

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

tabela_pt100["Erro_C"] = (
	tabela_pt100["T_real_C"] -
	tabela_pt100["T_estimado_C"]
	)

"""

5.6.4 Comparação Dinâmica Entre Sensores. pág. 298.

Nota sobre dt: o livro usa dt no modelo dinâmico, mas não declara o valor.
O passo de tempo correto é dt = 1, pois o vetor 'tempo' foi criado com
incremento de 1 segundo. Sem essa linha, o código não funciona.
"""

# Termopar
dt = 1          # passo de tempo (s)
tau_tc = 1.5
T_sensor = np.zeros_like(T_real)
for k in range(len(tempo)-1):
    T_sensor[k+1] = T_sensor[k] + (dt/tau_tc)*(T_real[k] - T_sensor[k])

# PT100
tau_pt100 = 6
T_pt_sensor = np.zeros_like(T_real)
for k in range(len(tempo)-1):
    T_pt_sensor[k+1] = T_pt_sensor[k] + (dt/tau_pt100)*(T_real[k] - T_pt_sensor[k])

# Tabela
tabela_comparativa = pd.DataFrame({
	"tempo_s": tempo,
	"T_real_C": T_real,
	"T_termopar_C": T_sensor,
	"T_pt100_C": T_pt_sensor
})
tabela_comparativa["Erro_termopar"] = (
tabela_comparativa["T_real_C"] -
tabela_comparativa["T_termopar_C"]
)
tabela_comparativa["Erro_pt100"] = (
tabela_comparativa["T_real_C"] -
tabela_comparativa["T_pt100_C"]
)	

"""

Mini-Projeto Integrador. pág. 299.

"""
# 1. Resolução Térmica
bits = 12
T_min = 0
T_max = 200
resolucao = (T_max - T_min) / (2**bits)
print("Resolução térmica:", resolucao, "°C")

# 2. Erro de Quantização - cálculos 

# 3. Implementação da Quantização
tabela_comparativa["T_quantizada"] = (
	np.round(
	tabela_comparativa["T_termopar_C"]/resolucao
	) * resolucao
)

"""

5.6.5 Simulação de Termistores NTC. pág.304

"""

# Exemplo computacional: Termistor NTC
R0 = 10000
T0 = 298.15
B = 3950
T_K = T_real + 273.15
R_ntc = R0 * np.exp(B*(1/T_K - 1/T0))
tabela_ntc = pd.DataFrame({
	"tempo_s": tempo,
	"T_real_C": T_real,
	"Resistencia_Ohm": R_ntc
})

# Inversão do Modelo do NTC.
T_estimado_K = 1 / (
	(1/T0) + (1/B)*np.log(R_ntc/R0)
	)
T_estimado_C = T_estimado_K - 273.15
# Adicionando à tabela
tabela_ntc["T_estimado_C"] = T_estimado_C
tabela_ntc["Erro_C"] = tabela_ntc["T_real_C"] - tabela_ntc["T_estimado_C"]
# Arredondando as colunas desejadas
tabela_ntc = tabela_ntc.round({
	"T_real_C": 4,
	"Resistencia_Ohm": 4,
	"T_estimado_C": 4,
	"Erro_C": 4
})
tabela_ntc





































