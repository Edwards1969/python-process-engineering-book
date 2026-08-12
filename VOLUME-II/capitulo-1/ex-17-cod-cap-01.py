# -*- coding: utf-8 -*-
"""

1.10.10 Exercício Computacional: Avaliação de Controladores com Saturaçã e 
Anti-Windup - pág. 60

"""
import numpy as np
import matplotlib.pyplot as plt
# Parâmetros do processo
a = 0.8
b = 1.5
dt = 0.05
tempo = np.arange(0, 60, dt)
# Saturação
u_min, u_max = 0.0, 5.0
# Controlador PI
Kp = 2.0
Ki = 0.8
def simular(anti_windup=False):
	y = 0.0
	integral = 0.0
	r = 3.0
	hist_y = []
	hist_u = []
	for t in tempo:
		# Perturbação em t = 20 s
		dist = 1.0 if t > 20 else 0.0
		erro = r - y
		integral += erro * dt
		u = Kp * erro + Ki * integral
		# Aplicar saturação
		u_sat = np.clip(u, u_min, u_max)
		# Anti-windup por clamping
		if anti_windup and (u != u_sat):
			integral -= erro * dt
		# Dinâmica do processo
		dy = -a * y + b * u_sat + dist
		y += dy * dt
		hist_y.append(y)
		hist_u.append(u_sat)
	return np.array(hist_y), np.array(hist_u)

# Simulações
y_sem, u_sem = simular(anti_windup=False)
y_com, u_com = simular(anti_windup=True)
# Gráficos em preto e branco, diferenciando por estilo de linha
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Resposta do sistema
ax1.plot(tempo, y_sem, label='Sem Anti-Windup',
color='black', linestyle='--', linewidth=1.8)
ax1.plot(tempo, y_com, label='Com Anti-Windup',
color='black', linestyle='-', linewidth=1.5)
ax1.set_ylabel('y(t)')
ax1.set_title('Resposta do Sistema com e sem Anti-Windup')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Sinal de controle
ax2.plot(tempo, u_sem, label='u(t) Sem Anti-Windup',
color='black', linestyle='--', linewidth=1.8)
ax2.plot(tempo, u_com, label='u(t) Com Anti-Windup',
color='black', linestyle='-', linewidth=1.5)
ax2.set_ylabel('u(t)')
ax2.set_xlabel('Tempo (s)')
ax2.set_title('Sinal de Controle com e sem Anti-Windup')
ax2.legend()
ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
