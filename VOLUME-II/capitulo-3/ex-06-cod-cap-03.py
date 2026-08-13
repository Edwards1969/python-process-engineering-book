# -*- coding: utf-8 -*-
"""

3.5 Modelagem Computacional da Pressão em um Vaso Pressurizado. - pág. 133

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parâmetros do vaso
V = 3.0        # volume (m³)
R = 287        # constante dos gases (ar) J/(kg.K)
T = 330        # temperatura absoluta (K)

# Vazões
m_in = 0.5     # kg/s (entrada constante)
Cv = 0.0007    # coeficiente da válvula de saída (ajustado)

# Tempo de simulação
dt = 0.01
tempo = np.arange(0, 250, dt)

# Vetores
P = np.zeros_like(tempo)

P[0] = 2e5     # pressão inicial (Pa)

# Simulação
for i in range(1, len(tempo)):
	P_safe = max(P[i-1], 1.0)  # evita raiz de número negativo
	m_out = Cv * np.sqrt(P_safe)
	dPdt = (R*T/V) * (m_in - m_out)
	P[i] = P[i-1] + dPdt * dt
    
	# pressão não pode ser negativa
	P[i] = max(P[i], 0.0)
tabela_vaso = pd.DataFrame({
	"tempo_s": tempo,
	"pressao_Pa": P,
	"pressao_bar": P/1e5
})
plt.figure(figsize=(8,5))
plt.plot(tempo, P/1e5, color="black", linewidth=1.8)
plt.xlabel("Tempo (s)")
plt.ylabel("Pressão (bar)")
plt.title("Dinâmica da Pressão em um Vaso Pressurizado")
plt.grid(True)
plt.show()

