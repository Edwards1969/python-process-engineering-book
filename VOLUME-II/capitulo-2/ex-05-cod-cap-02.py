# -*- coding: utf-8 -*-
"""

2.2.12 Simulação de Atrito Estático (Stiction) e Histerese. pág.92

"""
import numpy as np
import matplotlib.pyplot as plt
def simular_stiction(u_sinal, d):
	u_efetivo = np.zeros_like(u_sinal)
	u_last = u_sinal[0]
	for i in range(1, len(u_sinal)):
		# Logica do modelo de stiction (Atrito Estatico)
		if u_sinal[i] > u_last + d:
			u_efetivo[i] = u_sinal[i] - d
			u_last = u_efetivo[i]
		elif u_sinal[i] < u_last - d:
			u_efetivo[i] = u_sinal[i] + d
			u_last = u_efetivo[i]
		else:
			u_efetivo[i] = u_last
	return u_efetivo
# Gerando um sinal de controle senoidal (u)
t = np.linspace(0, 2*np.pi, 200)
u_controlador = 50 + 20 * np.sin(t) # Oscilando entre 30% e 70%
# Simulando com banda de atrito d = 5%
u_real = simular_stiction(u_controlador, 5.0)
# Plotagem
plt.figure(figsize=(10, 6))
plt.plot(u_controlador, color='black', linestyle='--', label='Sinal do Controlador (u)')
plt.plot(u_real, color='black', linewidth=2, label='Posicao Real da Valvula (u_efetivo)')
plt.title('Efeito de Stiction (Atrito Estatico) na Valvula')
plt.xlabel('Tempo (amostras)')
plt.ylabel('Abertura da Valvula (%)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

