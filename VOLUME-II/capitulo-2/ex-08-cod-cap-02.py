# -*- coding: utf-8 -*-
"""

2.4.5 Exemplo Prático: Contraste entre Vazão (Rápida) e Temperatura (Lenta). pág.

"""
import numpy as np
import matplotlib.pyplot as plt

# Parametros da Simulacao
dt = 0.1
tempo = np.arange(0, 500, dt)
K = 1.0          # Ganho unitario para ambos
tau_fast = 2.0   # Constante de tempo rapida (ex: Vazao)
tau_slow = 100.0 # Constante de tempo lenta (ex: Temperatura)

def simular_dinamicas():
	y_fast, y_slow = 0.0, 0.0
	res_fast, res_slow = [], []
	for t in tempo:
		u = 1.0 if t >= 5.0 else 0.0 # Degrau unitario em t=5s
        
		# Discretizacao de Primeira Ordem
		dy_fast = (dt / tau_fast) * (K * u - y_fast)
		dy_slow = (dt / tau_slow) * (K * u - y_slow)
		y_fast += dy_fast
		y_slow += dy_slow
		res_fast.append(y_fast)
		res_slow.append(y_slow)
	return res_fast, res_slow
y_f, y_s = simular_dinamicas()

# Plotagem Tecnica (Monocromatica)
plt.figure(figsize=(10, 6))
plt.plot(tempo, y_f, label='Processo Rapido ($\\tau=2s$)', color='black', linewidth=2)
plt.plot(tempo, y_s, label='Processo Lento ($\\tau=100s$)', color='black', linestyle='--')
plt.title('Comparativo de Dinamica: Processos Rapidos vs. Lentos')
plt.xlabel('Tempo (s)')
plt.ylabel('Resposta do Processo (%)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
