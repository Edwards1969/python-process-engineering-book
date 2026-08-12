# -*- coding: utf-8 -*-
"""

2.2.5 Exemplo Computacional: Processo Integrador vs. Autorregulado. pág.83

"""
import numpy as np
import matplotlib.pyplot as plt

# --- Parametros da Simulacao ---
dt = 0.1
tempo = np.arange(0, 100, dt)
A = 5.0          # Area do tanque (Integrador)
tau = 10.0       # Constante de tempo (Autorregulado)
K = 1.0          # Ganho do processo autorregulado

def simular_dinamicas():
	h_integrador = 1.0     # Nivel inicial
	y_autorregulado = 1.0  # Variavel inicial
	res_int = []
	res_aut = []
    
	for t in tempo:
		# Aplicamos um pequeno desbalanceamento constante (Degrau)
		# q_in > q_out em 0.2 unidades
		u = 0.2 
		# 1. Dinamica Integradora: h_k = h_k-1 + (dt/A) * u
		dh = (dt / A) * u
		h_integrador += dh
        
		# 2. Dinamica Autorregulada: y_k = y_k-1 + (dt/tau) * (K*u - y_k-1)
		# Note que aqui a variavel subtrai seu proprio valor, gerando equilibrio
		dy = (dt / tau) * (K * u - y_autorregulado)
		y_autorregulado += dy
		res_int.append(h_integrador)
		res_aut.append(y_autorregulado)
	return res_int, res_aut

# Execucao
h_int, y_aut = simular_dinamicas()

# --- Plotagem Comparativa ---
plt.figure(figsize=(10, 6))
plt.plot(tempo, h_int, label='Processo Integrador (Ex: Nível)', color='black', linewidth=2)
plt.plot(tempo, y_aut, label='Processo Autorregulado (Ex: Temperatura)', color='black', linestyle='--')
plt.title('Diferença Dinâmica: Integrador vs. Autorregulado')
plt.xlabel('Tempo (s)')
plt.ylabel('Resposta do Processo')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
