# -*- coding: utf-8 -*-
"""
5.6.5 Simulação de Termistores NTC — Continuação do Capítulo 5 - pág.304

Este script contém exatamente a sequência apresentada no livro,
com todas as variáveis necessárias para que o código funcione
de forma independente.
"""

import numpy as np
import pandas as pd

# Passo de tempo
dt = 1

# Vetor de tempo
tempo = np.arange(0, 600, dt)

# Temperatura real do processo (mesma usada nos itens anteriores)
T_real = 60 + 15 * np.sin(0.01 * tempo)

# Conversão para Kelvin
T_K = T_real + 273.15

"""
Simulação de Termistores NTC
Os termistores apresentam comportamento exponencial, descrito por:
R(T) = R0 * exp[B * (1/T - 1/T0)]
"""

# Parâmetros do NTC (exatamente como no livro)
R0 = 10000
T0 = 298.15
B = 3950

# Modelo direto do NTC
R_ntc = R0 * np.exp(B * (1/T_K - 1/T0))

# Tabela inicial (exatamente como no livro)
tabela_ntc = pd.DataFrame({
    "tempo_s": tempo,
    "T_real_C": T_real,
    "Resistencia_Ohm": R_ntc
})

"""
Inversão do Modelo do NTC
T = 1 / (1/T0 + (1/B)*ln(R/R0))
"""

# Modelo inverso (exatamente como no livro)
T_estimado_K = 1 / (
    (1/T0) + (1/B)*np.log(R_ntc/R0)
)

T_estimado_C = T_estimado_K - 273.15

# Adicionando à tabela (exatamente como no livro)
tabela_ntc["T_estimado_C"] = T_estimado_C
tabela_ntc["Erro_C"] = tabela_ntc["T_real_C"] - tabela_ntc["T_estimado_C"]

# Arredondando as colunas desejadas (exatamente como no livro)
tabela_ntc = tabela_ntc.round({
    "T_real_C": 4,
    "Resistencia_Ohm": 4,
    "T_estimado_C": 4,
    "Erro_C": 4
})

tabela_ntc
