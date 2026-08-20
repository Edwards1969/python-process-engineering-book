# -*- coding: utf-8 -*-
"""

1.5.1 Comparação Evolutiva: De P para PI e PID. - pág. 18-20

"""
import numpy as np
import matplotlib.pyplot as plt
# Configuracoes de referencia e tempo
SP = 6.0
dt = 0.05
tempo = np.arange(0, 40, dt)
# Parametros do processo (Modelo de Segunda Ordem)
a, b = 0.5, 0.2  
def simular_pid(Kp, Ki, Kd):
	h, h_dot = 0.0, 0.0
	erro_anterior = SP - h
	integral_erro = 0.0
	resposta = []
	for t in tempo:
		# 1. Calculo do Erro e suas componentes discretas
		erro = SP - h
		integral_erro += erro * dt
		dedt = (erro - erro_anterior) / dt
		# 2. Lei de Controle PID Completa
		u = Kp * erro + Ki * integral_erro + Kd * dedt
		# 3. Dinamica do processo (Aceleração)
		h_ddot = u - a*h_dot - b*h
		# 4. Integracao numerica (Metodo de Euler)
		h_dot = h_dot + h_ddot * dt
		h = h + h_dot * dt
		resposta.append(h)
		erro_anterior = erro
	return resposta
# Comparacao das combinacoes de acoes (Evolução)
resp_p   = simular_pid(Kp=2.0, Ki=0.0,  Kd=0.0)  
resp_pi  = simular_pid(Kp=2.0, Ki=0.15, Kd=0.0)  
resp_pid = simular_pid(Kp=2.0, Ki=0.15, Kd=2.5)  
# Plotagem Monocromática para Impressão
plt.figure(figsize=(10, 5))
plt.plot(tempo, resp_p, color='black', linestyle='-', 
label='Controlador P (Rápido, mas com Offset)')
plt.plot(tempo, resp_pi, color='black', linestyle='--', 
label='Controlador PI (Sem Offset, mas Oscilatório)')
plt.plot(tempo, resp_pid, color='black', linestyle='-.', linewidth=2,
label='Controlador PID (Rápido, Preciso e Estável)')
plt.axhline(SP, color='black', linestyle=':', label='Setpoint')
plt.xlabel('Tempo (s)')
plt.ylabel('Nível h(t)')
plt.title('Comparação entre as Ações de Controle: P vs PI vs PID')
plt.legend(loc='lower right')
plt.grid(True, alpha=0.3)
plt.show()

