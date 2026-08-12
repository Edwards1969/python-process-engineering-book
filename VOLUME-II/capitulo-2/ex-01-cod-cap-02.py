# -*- coding: utf-8 -*-
"""

2.4.2 = Exemplo Computacional: O Desafio do Atraso de Transporte. - pág. 78-79

"""
import numpy as np
import matplotlib.pyplot as plt
# --- Configuracoes da Simulacao ---
dt = 0.05
tempo = np.arange(0, 60, dt) # Tempo total reduzido para focar no transiente
SP = 1.0        
tau = 3.0       
def simular_tempo_morto(L_segundos, Kp, Ki):
	y = 0.0
	integral_erro = 0.0
	tamanho_buffer = int(L_segundos / dt)
	buffer_u = [0.0] * (tamanho_buffer + 1)
	lista_y = []
	for t in tempo:
		erro = SP - y
		integral_erro += erro * dt
		# Sintonia fixa para observar a degradacao
		u_calculado = Kp * erro + Ki * integral_erro
		u_final = np.clip(u_calculado, 0, 5) 
		buffer_u.append(u_final)
		u_atrasado = buffer_u.pop(0)
		dy = (dt / tau) * (u_atrasado - y)
		y += dy
		lista_y.append(y)
	return lista_y
# --- Testando valores proximos para melhor escala grafica ---
# Kp e Ki ajustados para mostrar oscilacao sem explodir o grafico
y_1s = simular_tempo_morto(L_segundos=1.0, Kp=1.2, Ki=0.3)
y_2s = simular_tempo_morto(L_segundos=2.0, Kp=1.2, Ki=0.3)
y_3s = simular_tempo_morto(L_segundos=3.0, Kp=1.2, Ki=0.3)
# --- Plotagem com Escala Harmonizada ---
plt.figure(figsize=(10, 6))
plt.plot(tempo, y_1s, label='Atraso L = 1s', color='black', linestyle=':')
plt.plot(tempo, y_2s, label='Atraso L = 2s', color='black', linestyle='--')
plt.plot(tempo, y_3s, label='Atraso L = 3s', color='black', linewidth=2)
plt.axhline(SP, color='black', linestyle='-.', alpha=0.5, label='Setpoint')
plt.title('Sensibilidade do PID ao Incremento do Tempo Morto')
plt.xlabel('Tempo (s)')
plt.ylabel('Resposta y(t)')
plt.legend(loc='lower right')
plt.grid(True, alpha=0.3)
plt.show()

