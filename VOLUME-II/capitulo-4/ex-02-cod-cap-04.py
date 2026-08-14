# -*- coding: utf-8 -*-
"""

4.6 Simulação Temporal da Vazão e Volume Acumulado. - pág. 178

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Criando uma simulação de tempo (0 a 60 s)
tempo = np.arange(0, 61, 1)

# Simulando uma vazão variável (m³/s)
vazao = 0.02 + 0.005 * np.sin(0.2 * tempo)

# Criando a tabela
tabela = pd.DataFrame({
		"Tempo_s": tempo,
		"Vazao_m3_s": vazao
	})

# Cálculo do volume acumulado ($m³$)
# Integração ponto a ponto pelo método dos trapézios
volume = [0]  # volume inicial

for i in range(1, len(tabela)):
	v1 = tabela["Vazao_m3_s"].iloc[i-1]
	v2 = tabela["Vazao_m3_s"].iloc[i]
	dt = tabela["Tempo_s"].iloc[i] - tabela["Tempo_s"].iloc[i-1]
	volume.append(volume[-1] + (v1 + v2)/2 * dt)
tabela["Volume_m3"] = volume
	
print(tabela)

# Gráfico da Vazão e do Volume Acumulado
plt.figure(figsize=(10,5))
plt.plot(tabela["Tempo_s"], tabela["Vazao_m3_s"], label="Vazão (m³/s)")
plt.xlabel("Tempo (s)")
plt.ylabel("Vazão (m³/s)")
plt.title("Variação Temporal da Vazão")
plt.grid(True)
plt.legend()
plt.show()

# Gráfico do volume acumulado
plt.figure(figsize=(10,5))
plt.plot(tabela["Tempo_s"], tabela["Volume_m3"], color="red",
label="Volume acumulado (m³)")
plt.xlabel("Tempo (s)")
plt.ylabel("Volume (m³)")
plt.title("Volume Acumulado ao Longo do Tempo")
plt.grid(True)
plt.legend()
plt.show()












