# -*- coding: utf-8 -*-
"""

Exemplo Prático: Implementação Discreta do PID. pág.465

"""
import numpy as np
import matplotlib.pyplot as plt
# Parâmetros do processo
tau = 5.0
# Parâmetros do PID
Kc = 2.0
tauI = 3.0
tauD = 0.5
# Tempo contínuo
dt = 0.001
t_cont = np.arange(0, 40, dt)
# Tempo discreto
Ts = 0.1
t_disc = np.arange(0, 40, Ts)
# Setpoint
sp = 1.0
# -----------------------------
# PID CONTÍNUO (simulação Euler)
# -----------------------------
y = 0.0
I = 0.0
e_prev = 0.0
y_cont = []
for k in range(len(t_cont)):
	e = sp - y
	I += e * dt
	D = (e - e_prev) / dt
	u = Kc * (e + (1/tauI)*I + tauD*D)
	y += dt * ((-y + u) / tau)
	y_cont.append(y)
	e_prev = e
# -----------------------------
# PID DISCRETO (incremental)
# -----------------------------
y = 0.0
u = 0.0
e_prev = 0.0
e_prev2 = 0.0
y_disc = []
for k in range(len(t_disc)):
	e = sp - y
	du = Kc*((e - e_prev) + (Ts/tauI)*e + (tauD/Ts)*(e - 2*e_prev + e_prev2))
	u += du
	y += Ts*((-y + u)/tau)
	y_disc.append(y)
	e_prev2 = e_prev
	e_prev = e
# -----------------------------
# GRÁFICO
# -----------------------------
plt.figure(figsize=(9,5))
plt.plot(t_cont, y_cont, 'k--', label='PID Contínuo')
plt.plot(t_disc, y_disc, 'k-', linewidth=2, label='PID Discreto (incremental)')
plt.legend()
plt.grid(True, linestyle=':')
plt.title('Comparação: PID Contínuo vs PID Discreto (Incremental)')
plt.xlabel('Tempo (s)')
plt.ylabel('Saída')
plt.tight_layout()
plt.show()

