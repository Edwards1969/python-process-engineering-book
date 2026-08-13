# -*- coding: utf-8 -*-
"""

2.6.2 Exemplo Prático: Determinação do Ganho Crítico e Robustez. pág. 113

"""
import numpy as np
import matplotlib.pyplot as plt
# Parametros do Processo
K, tau, L = 1.0, 10.0, 2.0
dt = 0.05
tempo = np.arange(0, 100, dt)
atraso_indices = int(L / dt)
def simular_estabilidade(Kp):
	y = np.zeros(len(tempo))
	u = np.zeros(len(tempo))
	erro = np.zeros(len(tempo))
	setpoint = 1.0
	for k in range(1, len(tempo)):
		# Calculo do Erro
		erro[k] = setpoint - y[k-1]
	# Controlador Proporcional
		u[k] = Kp * erro[k]
		# Processo com Tempo Morto: y(t) depende de u(t-L)
		if k > atraso_indices:
			u_atrasado = u[k - atraso_indices]
		else:
			u_atrasado = 0
		# Equacao Diferencial (Euler)
		dy = (K * u_atrasado - y[k-1]) / tau * dt
		y[k] = y[k-1] + dy
	return y
# Testando tres cenarios de Ganho
y_estavel = simular_estabilidade(Kp=5.0)   # Margem segura
y_limite  = simular_estabilidade(Kp=8.2)   # Proximo ao Ganho Critico
y_instavel = simular_estabilidade(Kp=12.0) # Ultrapassou a margem
# Plotagem Tecnica (Monocromatica)
plt.figure(figsize=(10, 6))
plt.plot(tempo, y_estavel, label='Estavel ($K_p=5$)', color='black', linestyle='-')
plt.plot(tempo, y_limite, label='Limite ($K_p=8.2$)', color='black', linestyle='--')
plt.plot(tempo, y_instavel, label='Instavel ($K_p=12$)', color='black', linestyle=':')
plt.axhline(y=1.0, color='gray', linewidth=0.5, linestyle='-')
plt.title('Analise de Estabilidade: Efeito do Ganho Proporcional')
plt.xlabel('Tempo (s)')
plt.ylabel('Resposta do Processo (PV)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.ylim(0, 2.5)
plt.show()
