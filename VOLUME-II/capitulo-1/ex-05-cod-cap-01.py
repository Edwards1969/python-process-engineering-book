# -*- coding: utf-8 -*-
"""

1.4.1 Exemplo Prático: Ação Derivativa como Amortecimento, - pág.14-16

"""
import numpy as np
import matplotlib.pyplot as plt
# Parâmetros de referência e tempo
SP = 6.0
dt = 0.05
tempo = np.arange(0, 40, dt)
# Parâmetros do processo (Segunda Ordem)
# Equação: h'' + a*h' + b*h = u
a = 0.4  # Baixo amortecimento natural
b = 0.2  # Rigidez do sistema
def simular_derivativo(Kc, Kd):
	h = 0.0             # Nível inicial
	h_dot = 0.0         # Velocidade inicial
	erro_anterior = SP - h
	resposta = []
	for t in tempo:
		# 1. Cálculo do Erro Atual
		erro = SP - h
		# 2. Cálculo da Derivada Discretizada (Taxa de Variação)
		# dedt representa a velocidade de aproximação do erro
		dedt = (erro - erro_anterior) / dt
		# 3. Ação de Controle PD (Proporcional-Derivativa)
		u = Kc * erro + Kd * dedt
		# 4. Equação Diferencial do Processo (Cálculo da Aceleração)
		h_ddot = u - a*h_dot - b*h
		# 5. Integração Numérica (Método de Euler)
		h_dot = h_dot + h_ddot * dt
		h = h + h_dot * dt
		# Armazenamento e atualização para o próximo ciclo
		resposta.append(h)
		erro_anterior = erro
	return resposta
# Simulações variando o ganho derivativo com Kc fixo e alto
resp_p_puro   = simular_derivativo(Kc=2.5, Kd=0.0)
resp_pd_baixo = simular_derivativo(Kc=2.5, Kd=1.5)
resp_pd_alto  = simular_derivativo(Kc=2.5, Kd=3.0)
# Plotagem Monocromática para Impressão
plt.figure(figsize=(10, 5))
plt.plot(tempo, resp_p_puro, color='black', linestyle='-', 
label=r'$K_{d}=0$ (Oscilatório)')
plt.plot(tempo, resp_pd_baixo, color='black', linestyle='--', 
label=r'$K_{d}=1.5$ (Amortecido)')
plt.plot(tempo, resp_pd_alto, color='black', linestyle='-.', 
label=r'$K_{d}=3.0$ (Super-amortecido)')
plt.axhline(SP, color='black', linestyle=':', label='Setpoint')
plt.xlabel('Tempo (s)')
plt.ylabel('h(t)')
plt.title('Efeito Amortecedor da Ação Derivativa (D)')
plt.legend(loc='lower right')
plt.grid(True, alpha=0.3)
plt.show()

