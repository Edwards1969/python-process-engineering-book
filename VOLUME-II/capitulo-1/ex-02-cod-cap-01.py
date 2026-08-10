# -*- coding: utf-8 -*-
"""
1.2.1 Exemplo Prático: Efeito do Ganho Proporcional do Nível 
de um Tanque - pág.4

"""
import numpy as np
import matplotlib.pyplot as plt

A = 2.0      # área transversal do tanque
R = 5.0      # resistência hidráulica
dt = 0.1     # passo de tempo
tempo = np.arange(0, 40, dt)
SP = 10.0    # setpoint do nível

def simular_controle_p(Kp):
	h = [0.0]   # nível inicial (h_0)
	
	for t in tempo[1:]:
		e = SP - h[-1]              # erro: e = SP - h
		q_in = Kp * e               # vazão de entrada: q_in = Kp * e
		q_out = h[-1] / R           # vazão de saída: q_out = h / R
		
		dh_dt = (q_in - q_out) / A  # equação 	diferencial: A dh/dt = q_in - q_out
		h_prox = h[-1] + dh_dt * dt # Euler: h_{t+1} = 	h_t + dh_dt * dt
		
		h.append(max(0, h_prox))    # nível não pode ser negativo
	
	return h

h_p_baixo = simular_controle_p(Kp=2.0)
h_p_alto  = simular_controle_p(Kp=5.0)

plt.figure(figsize=(10, 5))
plt.plot(tempo, h_p_baixo, label='Kp = 2.0 (Lento, maior offset)')
plt.plot(tempo, h_p_alto,  label='Kp = 5.0 (Rápido, menor offset)')
plt.axhline(SP, color='r', linestyle=':', label='Setpoint')

plt.title('Controle Proporcional (P) em um Tanque de Nível')
plt.xlabel('Tempo (s)')
plt.ylabel('Nível (m)')
plt.legend()
plt.grid(True)
plt.show()	
    
