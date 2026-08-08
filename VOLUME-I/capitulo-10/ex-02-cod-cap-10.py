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
