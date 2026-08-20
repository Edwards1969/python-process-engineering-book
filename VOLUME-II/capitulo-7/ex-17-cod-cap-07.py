# -*- coding: utf-8 -*-
"""

7.7.8 Considerações Práticas de Implementação. - pág.456

Exemplo Prático: Efeito da Saturação e do Windup -  pág.459

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

# Saturação
u_min, u_max = 0.0, 1.0

# Simulação
dt = 0.01
t = np.arange(0, 40, dt)
y = np.zeros_like(t)
I = 0.0
sp = 1.0

for k in range(1, len(t)):
	e = sp - y[k-1]
	I += (e / tauI) * dt
	u_pid = Kc * (e + I)
	u = np.clip(u_pid, u_min, u_max)
	y[k] = y[k-1] + processo(y[k-1], u) * dt
    
plt.figure(figsize=(9,5))
plt.plot(t, y, 'k-', label='Saída')
plt.plot(t, np.ones_like(t), 'k--', label='Setpoint')
plt.title('Windup causado pela Saturação')
plt.xlabel('Tempo (s)')
plt.ylabel('Saída')
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()

