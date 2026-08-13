# -*- coding: utf-8 -*-
"""

Simulação com Perturbação na Vazão de Entrada. - pág.137

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
Cv = 0.0007    # coeficiente da válvula de saída

# Tempo de simulação
dt = 0.01
tempo = np.arange(0, 250, dt)

# -------------------------------
# Simulação sem perturbação
# -------------------------------
P = np.zeros_like(tempo)
P[0] = 2e5     # pressão inicial (Pa)
for i in range(1, len(tempo)):
	P_safe = max(P[i-1], 1.0)  # evita raiz negativa
	m_out = Cv * np.sqrt(P_safe)
	dPdt = (R*T/V) * (m_in - m_out)
	P[i] = P[i-1] + dPdt * dt
	P[i] = max(P[i], 0.0)
tabela_vaso = pd.DataFrame({
	"tempo_s": tempo,
	"pressao_Pa": P,
	"pressao_bar": P/1e5
})

# -------------------------------
# Simulação com perturbação
# -------------------------------
P2 = np.zeros_like(tempo)
P2[0] = 2e5
for i in range(1, len(tempo)):
	# Perturbação: queda de vazão após 20 s
	if tempo[i] < 20:
		m_in_var = 0.8
	else:
		m_in_var = 0.3
	m_out = Cv * np.sqrt(P2[i-1])
	dPdt = (R*T/V) * (m_in_var - m_out)
	P2[i] = P2[i-1] + dPdt * dt
tabela_vaso_pert = pd.DataFrame({
	"tempo_s": tempo,
	"pressao_bar": P2/1e5
})

# -------------------------------
# Gráfico da perturbação
# -------------------------------
plt.figure(figsize=(8,5))
plt.plot(tempo, P2/1e5, color="black", linewidth=1.8)
plt.xlabel("Tempo (s)")
plt.ylabel("Pressão (bar)")
plt.title("Resposta do Vaso a uma Perturbação na Vazão de Entrada")
plt.grid(True)
plt.show()
