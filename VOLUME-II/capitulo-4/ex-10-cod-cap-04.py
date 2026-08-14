# -*- coding: utf-8 -*-

"""
4.13 Modelagem Computacional de Vazão em Tanques (Enchimento e 
Esvaziamento)  - pág. 210

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Enchimento de Tanque com Vazão Constante
# Parâmetros do tanque
A = 2.0          # área transversal (m²)
Q_in = 0.05      # vazão de entrada (m³/s)
h0 = 0.0         # nível inicial (m)

# Tempo de simulação
tempo = np.arange(0, 201, 1)

# Cálculo do nível
h = h0 + (Q_in / A) * tempo

tabela = pd.DataFrame({
	"Tempo_s": tempo,
	"Nivel_m": h
})

tabela

# Gráfico do Enchimento.
plt.figure(figsize=(10,5))
plt.plot(tabela["Tempo_s"], tabela["Nivel_m"], color="blue")
plt.xlabel("Tempo (s)")
plt.ylabel("Nível (m)")
plt.title("Enchimento de Tanque com Vazão Constante")
plt.grid(True)
plt.show()

# Esvaziamento de Tanque com Lei de Torricelli.
# Parâmetros
A = 2.0           # área do tanque (m²)
Ao = 0.01         # área do orifício (m²)
Cd = 0.62
g = 9.81
h0 = 2.0          # nível inicial (m)
	
# Tempo
dt = 0.1
tempo = np.arange(0, 200, dt)
	
h = []
nivel = h0
	
for t in tempo:
	Q_out = Cd * Ao * np.sqrt(2 * g * nivel)
	dhdt = -Q_out / A
	nivel = nivel + dhdt * dt
	nivel = max(nivel, 0)
	h.append(nivel)
	
tabela_esv = pd.DataFrame({
		"Tempo_s": tempo,
		"Nivel_m": h
	})

# Gráfico do Esvaziamento.
plt.figure(figsize=(10,5))
plt.plot(tabela_esv["Tempo_s"], tabela_esv["Nivel_m"], color="red")
plt.xlabel("Tempo (s)")
plt.ylabel("Nível (m)")
plt.title("Esvaziamento de Tanque pela Lei de Torricelli")
plt.grid(True)
plt.show()















