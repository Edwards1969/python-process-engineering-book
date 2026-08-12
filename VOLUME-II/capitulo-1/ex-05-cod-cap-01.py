# -*- coding: utf-8 -*-
"""

1.3.1 Exemplo Prático: Eliminação do Erro de Regime via Ação Integral. - pág.10-11

"""
import numpy as np
import matplotlib.pyplot as plt
# Configurações de referência e tempo
SP = 6.0
dt = 0.05
tempo = np.arange(0, 100, dt) # Tempo estendido para observar a estabilização
# Parâmetros do processo (Amortecimento e Rigidez)
# Equação: h'' + a*h' + b*h = u
a = 0.8  # Coeficiente de amortecimento
b = 0.2  # Coeficiente de rigidez/inércia

def simular_integral(Ki):
	h = 0.0         # Posição (nível) inicial
	h_dot = 0.0     # Velocidade inicial
	erro_acumulado = 0.0
	resposta = []
	for t in tempo:
		# 1. Cálculo do Erro (m)
		erro = SP - h
		# 2. Ação Integral Discretizada (Soma de Riemann)
		# erro_acumulado representa a área sob a curva do erro
		erro_acumulado += erro * dt
		u = Ki * erro_acumulado
		# 3. Equação Diferencial do Processo (Cálculo da Aceleração)
		h_ddot = u - a*h_dot - b*h
		# 4. Integração Numérica (Método de Euler)
		# Atualiza a velocidade (m/s)
		h_dot = h_dot + h_ddot * dt
		# Atualiza a posição/nível (m)
		h = h + h_dot * dt
		resposta.append(h)
	return resposta

# Ganhos integrais sintonizados para demonstrar convergência e estabilidade
Ki1, Ki2, Ki3 = 0.02, 0.05, 0.10
resp1 = simular_integral(Ki1)
resp2 = simular_integral(Ki2)
resp3 = simular_integral(Ki3)

# Plotagem Monocromática com Marcadores para Impressão
plt.figure(figsize=(10, 5))
plt.plot(tempo, resp1, color='black', linestyle='-',  
label=r'$K_{i1}$ (Ação lenta)')
plt.plot(tempo, resp2, color='black', linestyle='--', 
label=r'$K_{i2}$ (Ação moderada)')
plt.plot(tempo, resp3, color='black', linestyle=':',  
label=r'$K_{i3}$ (Ação agressiva)')
plt.axhline(SP, color='black', linestyle='-.', alpha=0.7, label='Setpoint')
plt.xlabel('Tempo (s)')
plt.ylabel('h(t)')
plt.title('Ação Integral: Eliminação do Erro de Regime Permanente (Offset)')
plt.legend(loc='lower right')
plt.grid(True, alpha=0.3)
plt.show()
    

