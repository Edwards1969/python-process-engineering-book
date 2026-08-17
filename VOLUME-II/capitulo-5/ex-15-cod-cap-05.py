# -*- coding: utf-8 -*-
"""

5.7 Integração Sensor + Modelo Térmico + Controle - pág. 306

5.7.4 Simulação do Processo Térmico

"""
# -*- coding: utf-8 -*-
"""
5.7.4 — Simulação do Processo Térmico (Malha Aberta)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Passo de tempo
dt = 0.1
tempo = np.arange(0, 200, dt)

# Parâmetros do processo
Tmax = 300      # temperatura máxima da fonte (°C)
tau = 25        # constante de tempo térmica
T = np.zeros_like(tempo)
T[0] = 25       # temperatura inicial

# Potência fixa (40%)
u = 0.4

# Simulação
for i in range(1, len(tempo)):
    T_fonte = Tmax * u
    T[i] = T[i-1] + (T_fonte - T[i-1]) * dt / tau

# Tabela
tabela_processo = pd.DataFrame({
    "tempo_s": tempo,
    "T_C": T
})

# Gráfico
plt.figure(figsize=(10,5))
plt.plot(tabela_processo["tempo_s"], tabela_processo["T_C"], color='black')
plt.xlabel("Tempo (s)")
plt.ylabel("Temperatura (°C)")
plt.title("Resposta do Processo Térmico em Malha Aberta")
plt.grid(True)
plt.show()
