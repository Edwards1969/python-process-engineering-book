# -*- coding: utf-8 -*-
"""

10.2.7 Criação e Exclusão de Colunas no DataFrame.  -  pág. 308-312

"""
import pandas as pd

tabela = pd.read_csv("propriedades_substancias.csv")

# Exemplo 1: Criação da coluna de Peso Específico (N/m^3):
tabela["Peso_Especifico_N_m3"] = tabela["Densidade_kg_m3"] * 9.81

# Exemplo 2: Convertendo viscosidade de cP para Pa.s.
    # 1 cP = 0.001 Pa.s
tabela["Viscosidade_Pa_s"] = tabela["Viscosidade_cP"] * 0.001

# Exemplo 3: Densidade Relativa (adimensional).
    # Considerando a densidade da água (rho_H2O) como 997 kg/m^3 (rho_rel = rho/rho_H2O)
tabela["Densidade_relativa"] = tabela["Densidade_kg_m3"]/ 997


