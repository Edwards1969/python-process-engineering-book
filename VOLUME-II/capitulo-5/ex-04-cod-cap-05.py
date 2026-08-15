# -*- coding: utf-8 -*-
"""

Exercício Computacional — Sensibilidade Radiativa. -mpág. 268

"""
import numpy as np
import pandas as pd

sigma = 5.67e-8
epsilon = 0.85
T_K = np.linspace(1173, 1373, 100)  # Kelvin
q = sigma * epsilon * T_K**4
tabela_radiacao = pd.DataFrame({
		"Temperatura_K": T_K,
		"Fluxo_W_m2": q
	})
tabela_radiacao["Variacao_percentual"] = (
	tabela_radiacao["Fluxo_W_m2"].pct_change()*100
	)

tabela_radiacao


