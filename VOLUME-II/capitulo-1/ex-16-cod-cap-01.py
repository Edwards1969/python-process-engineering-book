# -*- coding: utf-8 -*-
"""

1.10.8 Exercício Computacional: Controle de Interface em Separador Trifásico. - 57

"""
import numpy as np
import matplotlib.pyplot as plt
# --- Parametros do Sistema ---
A, rho_o, rho_a = 5.0, 850.0, 1000.0
ko, ka = 10.0, 12.0
dt = 0.1
tempo = np.arange(0, 400, dt)
# Setpoints
SP_ho = 0.8  # Interface oleo-agua
SP_hL = 1.5  # Nivel total (liquido-gas)
def simular_trifasico():
	ho, hL = 0.7, 1.4 # Niveis iniciais
	int_erro_o, int_erro_a = 0.0, 0.0
	res_ho, res_hL = [], []
	for t in tempo:
		# 1. Perturbacao: Aumento na entrada de agua em t=150s
		m_in_o = 5.0
		m_in_a = 4.0 if t < 150 else 9.0
		# 2. Controladores PI (Independentes)
		erro_o = SP_ho - ho
		erro_a = SP_hL - hL
		int_erro_o += erro_o * dt
		int_erro_a += erro_a * dt
		uo = np.clip(15.0 * erro_o + 0.5 * int_erro_o, 0, 100)
		ua = np.clip(18.0 * erro_a + 0.6 * int_erro_a, 0, 100)
		# 3. Dinamica das Interfaces (Tarefa 1)
		dho_dt = (m_in_o - ko * uo / 10) / (rho_o * A)
		dhL_dt = ((m_in_a - ka * ua / 10) / (rho_a * A)) + dho_dt
		ho += dho_dt * dt
		hL += dhL_dt * dt
		res_ho.append(ho)
		res_hL.append(hL)
	return res_ho, res_hL
# Execucao e Plotagem
ho, hL = simular_trifasico()
plt.figure(figsize=(10, 6))
plt.plot(tempo, ho, label='Interface Óleo-Água ($h_o$)', color='black', linestyle='--')
plt.plot(tempo, hL, label='Nível Total ($h_L$)', color='black', linewidth=2)
plt.axvline(150, color='grey', linestyle=':', label='Perturbação na Água')
plt.title('Controle Multivariável: Acoplamento em Separador Trifásico')
plt.xlabel('Tempo (s)')
plt.ylabel('Nível (m)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

