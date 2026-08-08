# -*- coding: utf-8 -*-
"""
10.2.1 Tabela de Referência: Propriedades de Substâncias Industriais. - pág.300-

"""
import pandas as pd

tabela = pd.read_csv("propriedades_substancias.csv")

# Acessando uma coluna.
tabela["Densidade_kg_m3"]

tabela[["Substancia", "Ponto_Ebulicao_C"]]

import os
os.getcwd()

# Acessando uma linha.
tabela.loc[0]

# Acessando um intervalo de linhas.
tabela.loc[5:8]

# Acessando elementos específicos.
tabela.loc[2, "Viscosidade_cP"]

# 10.2.6 Filtragem de Dados no DataFrame.

# Filtragem por uma condição.
tabela[tabela["Estado_25C"] == "Liquido" ]

tabela[tabela["Estado_25C"] == "Gasoso"]

tabela[tabela["Densidade_kg_m3"] > 900]

# Filtragem por múltiplas condições.
	# Garantindo que colunas numéricas estejam no formato correto.
tabela["Ponto_Ebulicao_C"] = pd.to_numeric(tabela["Ponto_Ebulicao_C"], errors="coerce")
tabela["Ponto_fusao_C"] = pd.to_numeric(tabela["Ponto_Fusao_C"], errors="coerce")
tabela["Massa_Molar_g_mol"] = pd.to_numeric(tabela["Massa_Molar_g_mol"], errors="coerce")
tabela["Viscosidade_cP"] = pd.to_numeric(tabela["Viscosidade_cP"], errors="coerce")


















