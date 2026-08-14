# -*- coding: utf-8 -*-
"""

4.14 Integração Entre Vazão, Nível e Dinâmica de Processos. - pág. 214

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parâmetros do tanque
A = 2.0          # área (m²)
Qout = 0.03      # vazão de saída (m³/s)
h0 = 0.5         # nível inicial (m)

# Tempo de simulação
dt = 0.1
tempo = np.arange(0, 200, dt)

# Variáveis
h = h0
historico = []

for t in tempo:
	# Degrau de vazão
	if t < 20:
	  Qin = 0.03
	else:
	  Qin = 0.06
	# Dinâmica do tanque
	dhdt = (Qin - Qout) / A
	h = h + dhdt * dt
	historico.append([t, h, Qin])
    
tabela = pd.DataFrame(historico, columns=["Tempo_s", "Nivel_m", "Qin"])

# Gráfico da Resposta do Nível.
plt.figure(figsize=(10,5))
plt.plot(tabela["Tempo_s"], tabela["Nivel_m"], label="Nível")
plt.axvline(20, color="gray", linestyle="--", label="Degrau de Vazão")
plt.xlabel("Tempo (s)")
plt.ylabel("Nível (m)")
plt.title("Resposta do Nível a um Degrau de Vazão")
plt.grid(True)
plt.legend()
plt.show()

















