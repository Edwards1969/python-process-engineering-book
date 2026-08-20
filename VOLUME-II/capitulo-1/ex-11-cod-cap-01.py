# -*- coding: utf-8 -*-
"""

1.10.1 Exemplo Introdutório: Controle deNível em um Tanque Simples com PID. - pág. 38

"""
import numpy as np
import matplotlib.pyplot as plt
# parâmetros do processo
A = 5.0        # área do tanque (m²)
k = 2.0        # coeficiente da válvula de saída
h_sp = 2.0     # setpoint (m)
h_max = 3.0    # altura máxima do tanque (m)
# controlador PID
Kp = 4.0
Ki = 0.8
Kd = 0.2
dt = 0.1
t_final = 80
t = np.arange(0, t_final, dt)
h = np.zeros_like(t)
u = np.zeros_like(t)
e_prev = 0
integral = 0
for i in range(1, len(t)):
	e = h_sp - h[i-1]
	integral += e * dt
	derivative = (e - e_prev) / dt
	e_prev = e
	# controlador atua na vazão de entrada
	u[i] = Kp*e + Ki*integral + Kd*derivative
	u[i] = np.clip(u[i], 0, 5.0)   # entrada limitada (m³/s)
	# saída depende do nível (modelo físico)
	qout = k * np.sqrt(max(h[i-1], 0))
	# balanço de massa
	dhdt = (u[i] - qout) / A
	h[i] = h[i-1] + dhdt * dt
	# limites físicos
	h[i] = max(0, min(h[i], h_max))
plt.plot(t, h)
plt.axhline(h_sp, color='r', linestyle='--')
plt.xlabel('Tempo (s)')
plt.ylabel('Nível (m)')
plt.title('Controle de Nível em Tanque com PID (modelo realista)')
plt.grid(True)
plt.show()

