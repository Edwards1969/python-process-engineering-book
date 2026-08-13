# -*- coding: utf-8 -*-
"""

2.3.5 Exemplo Prático: Tanques Interligados e Interação Multivariável. pág.100

"""
import numpy as np
import matplotlib.pyplot as plt
# Parametros do sistema
A1, A2 = 1.0, 1.0
R1, R2 = 2.0, 2.0
dt = 0.1
tempo = np.arange(0, 20, dt)
def simular_tanques_acoplados():
	h1, h2 = 0.0, 0.0  # Estados iniciais
	res_h1, res_h2 = [], []
	for i, t in enumerate(tempo):
		# Aplicamos um degrau em u1 no instante t=1s
		u1 = 1.0 if t >= 1.0 else 0.0
		# Equacoes diferenciais discretizadas (Euler)
		dh1 = (u1 - h1/R1) / A1 * dt
		dh2 = (h1/R1 - h2/R2) / A2 * dt
		h1 += dh1
		h2 += dh2
		res_h1.append(h1)
		res_h2.append(h2)
	return res_h1, res_h2
h1, h2 = simular_tanques_acoplados()
# Plotagem Tecnica
plt.figure(figsize=(10, 6))
plt.plot(tempo, h1, label='Nivel Tanque 1 ($h_1$)', color='black', linewidth=2)
plt.plot(tempo, h2, label='Nivel Tanque 2 ($h_2$)', color='black', linestyle='--')
plt.title('Resposta Dinamica em Processos Acoplados')
plt.xlabel('Tempo (s)')
plt.ylabel('Nivel (m)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

