# -*- coding: utf-8 -*-
"""

4.8 Detecção de Falhas e Ruídos em Sensores de Vazão. - pág.188-191

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Exemplo de Sinal com Ruído

tempo = np.arange(0, 101, 1)
vazao_real = 0.03 + 0.005 * np.sin(0.1 * tempo)
ruido = np.random.normal(0, 0.001, len(tempo))
vazao_medida = vazao_real + ruido
tabela = pd.DataFrame({
		"Tempo_s": tempo,
		"Vazao_m3_s": vazao_medida
	})

# Detecção de Valores Anômalos (Outliers).

media = tabela["Vazao_m3_s"].mean()
desvio = tabela["Vazao_m3_s"].std()
limite_superior = media + 3 * desvio
limite_inferior = media - 3 * desvio
tabela["Anomalia"] = (
	(tabela["Vazao_m3_s"] > limite_superior) |
	(tabela["Vazao_m3_s"] < limite_inferior)
	)

# Filtragem Digital do Sinal.
tabela["Vazao_filtrada"] = (
	tabela["Vazao_m3_s"].rolling(window=5).mean()
	)

# Visualização Gráfica.
plt.figure(figsize=(10,5))
plt.plot(tabela["Tempo_s"], tabela["Vazao_m3_s"],
label="Sinal com ruído", alpha=0.6)
plt.plot(tabela["Tempo_s"], tabela["Vazao_filtrada"],
label="Sinal filtrado", linewidth=2, color="red")
plt.xlabel("Tempo (s)")
plt.ylabel("Vazão (m³/s)")
plt.title("Filtragem Digital do Sinal de Vazão")
plt.grid(True)
plt.legend()
plt.show()





