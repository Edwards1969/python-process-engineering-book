# -*- coding: utf-8 -*-
"""

4.19 Instrumentação Inteligente e Indústria 4.0. pág. 245

"""
import pandas as pd
import numpy as np
	
# Simulação de dados em tempo real
tempo = np.arange(0, 600, 1)
vazao = 0.03 + 0.005*np.sin(0.02*tempo) + np.random.normal(0, 0.0005, len(tempo))

vazao = 0.03 + 0.005 * np.sin(0.02*tempo) 
+ np.random.normal(0, 0.005, len(tempo))

tabela = pd.DataFrame({
	"Tempo_s": tempo,
	"Vazao_m3_s": vazao
})
	
# Cálculo de estatísticas para dashboard
media = tabela["Vazao_m3_s"].mean()
desvio = tabela["Vazao_m3_s"].std()
maximo = tabela["Vazao_m3_s"].max()
minimo = tabela["Vazao_m3_s"].min()