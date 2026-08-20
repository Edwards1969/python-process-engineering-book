# -*- coding: utf-8 -*-
"""

1.10.2 Estudo de Caso: Controle de Nível em um Separadorde Produção.

"""
import numpy as np
import matplotlib.pyplot as plt
# --- Parametros do Separador e Simulacao ---
Area = 5.0          # Area transversal do separador (m2)
dt = 0.1            # Passo de tempo (s)
tempo = np.arange(0, 300, dt)
SP = 2.5            # Setpoint de nivel (m)
U_MAX = 20.0        # Vazao maxima da valvula de saida (m3/s)
def simular_separador(Kp, Ki, Kd):
	h = 2.0             # Nivel inicial (m)
	erro_anterior = SP - h
	integral_erro = 0.0
	lista_h = []
	lista_u = []
	for t in tempo:
		# 1. Definicao da Perturbacao (Golfada de liquido em t = 100s)
		q_in = 5.0 if t < 100 else 12.0
		# 2. Algoritmo PID com Anti-Windup (Clamping)
		erro = SP - h
		u_p = Kp * erro
		u_d = Kd * (erro - erro_anterior) / dt
		u_i_tentativa = integral_erro + (Ki * erro * dt)
		u_calc = u_p + u_i_tentativa + u_d
		# Logica de Clamping: so integra se nao estiver saturado
		if 0 < u_calc < U_MAX:
			integral_erro = u_i_tentativa
		u_final = np.clip(u_calc, 0, U_MAX)
		# 3. Dinamica do Processo (Balanço de Massa: dh/dt = (qin - qout) / Area)
		# Note que a valvula de saida (u_final) retira liquido (sinal negativo)
		dh_dt = (q_in - u_final) / Area
		h = h + dh_dt * dt
		# Garantir limites fisicos do tanque (vazio ou transbordando)
		h = max(0, min(h, 5.0)) 
		lista_h.append(h)
		lista_u.append(u_final)
		erro_anterior = erro
	return lista_h, lista_u
# --- Execucao das Simulacoes ---
# Sintonia 1: Apenas Proporcional
h_p, u_p = simular_separador(Kp=10.0, Ki=0.0, Kd=0.0)
# Sintonia 2: PID Ajustado
h_pid, u_pid = simular_separador(Kp=15.0, Ki=0.2, Kd=10.0)
# --- Visualizacao dos Resultados (Padrao Monocromatico) ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
# Grafico de Nivel
ax1.plot(tempo, h_p, label='Controle P (Offset)', color='black', linestyle='--')
ax1.plot(tempo, h_pid, label='Controle PID (Robusto)', color='black', linestyle='-', linewidth=2)
ax1.axhline(SP, color='black', linestyle=':', label='Setpoint')
ax1.set_ylabel('Nível (m)')
ax1.set_title('Controle de Nível sob Perturbação (Golfada de Entrada)')
ax1.legend(loc='upper right')
ax1.grid(True, alpha=0.3)
# Grafico de Abertura de Valvula
ax2.plot(tempo, u_p, color='black', linestyle='--', label='Saída P')
ax2.plot(tempo, u_pid, color='black', linestyle='-', label='Saída PID')
ax2.set_ylabel('Vazão de Saída (m³/s)')
ax2.set_xlabel('Tempo (s)')
ax2.axhline(U_MAX, color='black', linestyle='-.', label='Capacidade Máxima')
ax2.legend(loc='lower right')
ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

