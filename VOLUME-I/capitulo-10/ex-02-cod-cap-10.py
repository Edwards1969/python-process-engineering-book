# -*- coding: utf-8 -*-
"""

Operadores lógicos. - pág.304-305

"""
import pandas as pd

tabela = pd.read_csv("propriedades_substancias.csv")

# Filtragem por múltiplas condições.
	# Garantindo que colunas numéricas estejam no formato correto.
tabela["Ponto_Ebulicao_C"] = pd.to_numeric(tabela["Ponto_Ebulicao_C"], errors="coerce")
tabela["Ponto_fusao_C"] = pd.to_numeric(tabela["Ponto_Fusao_C"], errors="coerce")
tabela["Massa_Molar_g_mol"] = pd.to_numeric(tabela["Massa_Molar_g_mol"], errors="coerce")
tabela["Viscosidade_cP"] = pd.to_numeric(tabela["Viscosidade_cP"], errors="coerce")

# Selecione substância líquida com ponto de ebulição acima de 100 o^C.
tabela[
       (tabela["Estado_25C"]  == "Liquido") &
       (tabela["Ponto_Ebulicao_C"] > 100)    
       ]

# Selecione todas as linhas onde as substância é gasosa OU a massa é menor que 40 g/mol.
tabela[
       (tabela["Estado_25C"] == "Gasoso") |
       (tabela["Massa_Molar_g_mol"] < 40)
       ]

# Para identificar linhas com valores ausentes.
tabela[tabela["Viscosidade_cP"].isna()]

# Para selecionar apenas linhas com valores válidos:
tabela[tabela["Viscosidade_cP"].notna()]

# Para selecionar substâncias cujo ponto de fusão esta entre -100o^C e 10o^C.
tabela[
       (tabela["Ponto_Fusao_C"] >= -100) &
       (tabela["Ponto_Fusao_C"] <= 10)
       ]






