# -*- coding: utf-8 -*-
"""

1.5.2 WExeplo Prático: A Sinergia das Ações P, I e D. - pág.20-23

"""
import numpy as np
import matplotlib.pyplot as plt
# Configuracoes de simulacao
SP = 6.0
dt = 0.05
tempo = np.arange(0, 60, dt)
# Parametros do processo (Modelo de Segunda Ordem)
# Equação: h'' + a*h' + b*h = u + disturbio
a, b = 0.5, 0.2
def simular_analise(Kp, Ki, Kd):
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
		# 3. Perturbacao em t = 20s (Ex: aumento subito na vazao de saida)
		disturbio = 1.5 if t > 20 else 0.0
		# 4. Dinamica do processo (Calculo da Aceleracao)
		h_ddot = (u + disturbio) - a*h_dot - b*h
		# 5. Integracao numerica (Metodo de Euler)
		h_dot = h_dot + h_ddot * dt
		h = h + h_dot * dt
		# Atualização para o próximo passo
		resposta.append(h)
		erro_anterior = erro
	return resposta
# Gerando tres cenarios para analise de sintonia
# 1. Sintonia Equilibrada (PID)
resp_bom = simular_analise(Kp=2.5, Ki=0.2,  Kd=3.0)
# 2. Kp Baixo (Resposta lenta ao setpoint e ao disturbio)
resp_kp_baixo = simular_analise(Kp=0.8, Ki=0.2,  Kd=3.0)
# 3. Ki Baixo (Dificuldade em eliminar o erro residual da perturbacao)
resp_ki_baixo = simular_analise(Kp=2.5, Ki=0.02, Kd=3.0)

# Plotagem Monocromática para o Livro
plt.figure(figsize=(10, 6))
plt.plot(tempo, resp_bom, label='Sintonia Equilibrada', 
color='black', linestyle='-', linewidth=2)
plt.plot(tempo, resp_kp_baixo, label='Kp Baixo (Lento)', 
color='black', linestyle='--', linewidth=1.5)
plt.plot(tempo, resp_ki_baixo, label='Ki Baixo (Erro Residual)', 
color='black', linestyle=':', linewidth=1.5)
plt.axhline(SP, color='black', linestyle='-.', alpha=0.7, label='Setpoint')
plt.axvline(20, color='black', linestyle='-', alpha=0.2) 
plt.text(21, 5.2, 'Início da Perturbação', fontsize=10, weight='bold')
plt.title('Análise de Malha Fechada: Sinergia PID e Rejeição de Carga')
plt.xlabel('Tempo (s)')
plt.ylabel('h(t)')
plt.legend(loc='lower right')
plt.grid(True, alpha=0.3)
plt.show()
