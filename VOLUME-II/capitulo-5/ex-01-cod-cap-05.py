# -*- coding: utf-8 -*-
"""

5.3 Faixas de Temperatura e Aplicações Industriais. pág. 256-258

"""
import numpy as np
import pandas as pd

T = np.array([-200, -180, -160, -140, -120])
Cp = np.array([0.8, 0.95, 1.1, 1.35, 1.6])

tabela_crio = pd.DataFrame({
		"Temperatura_C": T,
		"Cp_kJ_kgK": Cp
	})

# Interpolação
T_interp = np.linspace(-200, -120, 50)
Cp_interp = np.interp(T_interp, T, Cp)
tabela_interp = pd.DataFrame({
		"Temperatura_C": T_interp,
		"Cp_interp_kJ_kgK": Cp_interp
	})


