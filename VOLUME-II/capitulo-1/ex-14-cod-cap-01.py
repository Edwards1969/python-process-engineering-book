# -*- coding: utf-8 -*-
"""

1.10.3 Controle de Nível em Tanque de Primeira Ordem (Não Linear).  -  pág.45

"""
import numpy as np
import matplotlib.pyplot as plt
# --- Parametros do Tanque ---
A = 2.0             # Area da secao transversal (m2)
C = 0.5             # Coeficiente de descarga (m^2.5/s)	
dt = 0.1            # Passo de tempo (s)
tempo = np.arange(0, 400, dt)
SP = 3.0            # Setpoint de nivel (m)
def simular_tanque_gravidade(Kp, Ki, Kd):
	h = 0.5             # Nivel inicial (m)
	erro_anterior = SP - h
	integral_erro = 0.0
	lista_h = []
	lista_q_in = []
	for t in tempo:
		# 1. Algoritmo PID com Clamping (Anti-Windup)
		erro = SP - h
		u_p = Kp * erro
		u_d = Kd * (erro - erro_anterior) / dt
		u_i_tentativa = integral_erro + (Ki * erro * dt)
		q_calc = u_p + u_i_tentativa + u_d
		# Limite fisico da bomba de entrada (0 a 2.0 m3/s)
		q_in = np.clip(q_calc, 0, 2.0)
		# Logica de Clamping
		if q_in == q_calc:
			integral_erro = u_i_tentativa
		# 2. Dinamica do Processo (Nao Linear)
		# dh/dt = (qin - C*sqrt(h)) / A
		dh_dt = (q_in - C * np.sqrt(max(h, 0))) / A
		h = h + dh_dt * dt
		lista_h.append(h)
		lista_q_in.append(q_in)
		erro_anterior = erro
	return lista_h, lista_q_in
# --- Teste de Sintonia ---
# 1. P Puro (com offset esperado devido a saida por gravidade)
h_p, _ = simular_tanque_gravidade(Kp=0.8, Ki=0.0, Kd=0.0)
# 2. PI (eliminando o offset)
h_pi, _ = simular_tanque_gravidade(Kp=0.8, Ki=0.05, Kd=0.0)
# 3. PID (melhorando o amortecimento)
h_pid, q_pid = simular_tanque_gravidade(Kp=1.2, Ki=0.05, Kd=5.0)
# --- Graficos (Padrao Monocromatico para impressao) ---
plt.figure(figsize=(10, 6))
plt.plot(tempo, h_p,   label='Proporcional (P)', color='black', linestyle='--')
plt.plot(tempo, h_pi,  label='Proporcional-Integral (PI)', color='black', linestyle='-.')
plt.plot(tempo, h_pid, label='PID Completo', color='black', linewidth=2)
plt.axhline(SP, color='black', linestyle=':', label='Setpoint')
plt.title('Controle de Nível: Saída por Gravidade (Não Linear)')
plt.xlabel('Tempo (s)')
plt.ylabel('Nível h(t)')
plt.legend(loc='lower right')
plt.grid(True, alpha=0.3)
plt.show()

