# -*- coding: utf-8 -*-
"""

1.11.4 Exercício Computacional: Comparação entre Malha Simple, Cascata e 
Feedforward. pág. 66 

"""
import numpy as np
import matplotlib.pyplot as plt
# Parâmetros do processo
A = 5.0
kv = 0.8
dt = 0.1
tempo = np.arange(0, 120, dt)
# Setpoint de nível
SP = 2.0
# Ganhos dos controladores
Kp = 3.0
Ki = 0.4
# Ganhos da malha interna (cascata)
Kp_v = 2.0
Ki_v = 0.3
# Ganho feedforward
Kff = 0.9
def simular(arquitetura):
	h = 1.5
	integral = 0.0
	integral_v = 0.0
	hist_h = []
	hist_u = []
	for t in tempo:
		# Perturbação na vazão de entrada
		q_in = 1.0 if t < 40 else 2.5
		# Controle
		if arquitetura == "simples":
			erro = SP - h
			integral += erro * dt
			u = Kp * erro + Ki * integral
		elif arquitetura == "cascata":
			# Controlador primário (nível)
			erro = SP - h
			integral += erro * dt
			SP_vazao = Kp * erro + Ki * integral
			# Controlador secundário (vazão)
			erro_v = SP_vazao - (kv * 1.0)  # vazão medida fictícia
			integral_v += erro_v * dt
			u = Kp_v * erro_v + Ki_v * integral_v
		elif arquitetura == "feedforward":
			erro = SP - h
			integral += erro * dt
			# Controle feedback (PI)
			u_fb = Kp * erro + Ki * integral
			# Ação feedforward baseada na perturbação
			# Compensa diretamente o aumento de q_in
			u_ff = (q_in / kv) * 100   # abre a válvula proporcional à carga
			# Combinação das ações
			u = u_fb + u_ff
		# Saturação
		u = np.clip(u, 0, 100)
		# Vazão de saída
		q_out = kv * (u / 100)
		# Dinâmica do tanque
		dh = (q_in - q_out) / A
		h += dh * dt
		hist_h.append(h)
		hist_u.append(u)
	return np.array(hist_h), np.array(hist_u)

# Simulações
h_s, u_s = simular("simples")
h_c, u_c = simular("cascata")
h_f, u_f = simular("feedforward")

# Gráficos em preto e branco
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
ax1.plot(tempo, h_s, linestyle='--', color='black', label='Malha Simples')
ax1.plot(tempo, h_c, linestyle='-', color='black', label='Cascata')
ax1.plot(tempo, h_f, linestyle=':', color='black', label='Feedforward')
ax1.axhline(SP, linestyle='-.', color='black', label='Setpoint')
ax1.set_ylabel('Nível (m)')
ax1.set_title('Comparação de Arquiteturas de Controle')
ax1.legend()
ax1.grid(True, alpha=0.3)
ax2.plot(tempo, u_s, linestyle='--', color='black', label='u(t) Simples')
ax2.plot(tempo, u_c, linestyle='-', color='black', label='u(t) Cascata')
ax2.plot(tempo, u_f, linestyle=':', color='black', label='u(t) Feedforward')
ax2.set_ylabel('Abertura (%)')
ax2.set_xlabel('Tempo (s)')
ax2.set_title('Esforço de Controle')
ax2.legend()
ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

