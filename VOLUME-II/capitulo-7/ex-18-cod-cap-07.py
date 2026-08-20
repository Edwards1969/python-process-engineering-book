# -*- coding: utf-8 -*-
"""

Exemplo Prático: Anti-Windup por Back-Calculation. pág. 461

"""
import numpy as np
import matplotlib.pyplot as plt
# Processo
tau = 5.0
def processo(y, u):
	return (-y + u) / tau
# Controlador PI
Kc = 2.0
tauI = 3.0
Kaw = 1 / tauI
# Saturação
u_min, u_max = 0.0, 1.0
# Tempo
dt = 0.01
t = np.arange(0, 40, dt)
sp = 1.0
# Sem anti-windup
y1 = np.zeros_like(t)
I1 = 0.0
for k in range(1, len(t)):
	e = sp - y1[k-1]
	I1 += (e / tauI) * dt
	u_pid = Kc * (e + I1)
	u = np.clip(u_pid, u_min, u_max)
	y1[k] = y1[k-1] + processo(y1[k-1], u) * dt
# Com anti-windup
y2 = np.zeros_like(t)
I2 = 0.0
for k in range(1, len(t)):
	e = sp - y2[k-1]
	u_pid = Kc * (e + I2)
	u = np.clip(u_pid, u_min, u_max)
	I2 += ((e / tauI) + Kaw * (u - u_pid)) * dt
	y2[k] = y2[k-1] + processo(y2[k-1], u) * dt
plt.figure(figsize=(9,5))
plt.plot(t, y1 - 0.02, 'k--', label='Sem Anti-Windup')
plt.plot(t, y2, 'k-', linewidth=2, label='Com Anti-Windup')
plt.legend()
plt.grid(True, linestyle=':')
plt.title('Comparação: Com e Sem Anti-Windup')
plt.xlabel('Tempo (s)')
plt.ylabel('Saída')
plt.tight_layout()
plt.show()

