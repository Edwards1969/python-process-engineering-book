# -*- coding: utf-8 -*-
"""

2.5.8 Exemplo Prático: Filtragem Digital e Atraso de Fase. pág. 109

"""
import numpy as np
import matplotlib.pyplot as plt

# Configuracao da simulacao
dt = 0.1
t = np.arange(0, 50, dt)
y_real = np.where(t > 5, 1.0, 0.0) # Degrau unitario puro

# Gerando ruido gaussiano (sigma = 0.05)
np.random.seed(42)
ruido = np.random.normal(0, 0.05, len(t))
y_ruidoso = y_real + ruido
def aplicar_filtro(sinal, alpha):
	y_f = np.zeros_like(sinal)
	for k in range(1, len(sinal)):
		y_f[k] = (1 - alpha) * y_f[k-1] + alpha * sinal[k]
	return y_f

# Aplicando dois niveis de filtragem
y_suave = aplicar_filtro(y_ruidoso, alpha=0.2)  # Filtragem leve
y_forte = aplicar_filtro(y_ruidoso, alpha=0.05) # Filtragem agressiva

# Plotagem
plt.figure(figsize=(10, 6))
plt.plot(t, y_ruidoso, color='silver', label='Sinal Ruidoso (Sensor)')
plt.plot(t, y_real, color='black', linestyle='--', label='Sinal Real (Invisivel)')
plt.plot(t, y_suave, color='black', linewidth=1, label='Filtro Leve (alpha=0.2)')
plt.plot(t, y_forte, color='black', linewidth=2, label='Filtro Forte (alpha=0.05)')
plt.title('Impacto da Filtragem Passa-Baixa em Sinais Ruidosos')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

