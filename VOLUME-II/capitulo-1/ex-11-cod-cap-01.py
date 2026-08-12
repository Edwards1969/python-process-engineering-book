# -*- coding: utf-8 -*-
"""

1.8.1 Exemplo Prático: Saturação do Atuador e Técnica Anti-windup. - pág.34

"""
import numpy as np
import matplotlib.pyplot as plt
# --- Configuracoes de simulacao ---
SP = 12.0  # Setpoint
dt = 0.1
tempo = np.arange(0, 100, dt)
U_MAX = 10.0  # Limite de saturacao
# Parametros do processo (Modelo de Segunda Ordem)
a, b = 0.5, 0.2
def simular_pid_pratico(anti_windup=False):
	h, h_dot = 0.0, 0.0
	erro_anterior = SP - h
	integral_erro = 0.0
	resposta = []
	acao_u = []
	for t in tempo:
		erro = SP - h
		u_p = 2.0 * erro
		u_d = 1.5 * ((erro - erro_anterior) / dt)
		# Logica Anti-Windup
		u_antes_da_integral = u_p + u_d + (0.5 * integral_erro)
		if anti_windup:
			if not ((u_antes_da_integral >= U_MAX and erro > 0) 
			or 
				(u_antes_da_integral <= 0 and erro < 0)):
				integral_erro += erro * dt
		else:
			integral_erro += erro * dt 
		u_calculado = u_p + (0.5 * integral_erro) + u_d
		u_final = np.clip(u_calculado, 0, U_MAX)
		h_ddot = u_final - a*h_dot - b*h
		h_dot = h_dot + h_ddot * dt
		h = h + h_dot * dt
		resposta.append(h)
		acao_u.append(u_final)
		erro_anterior = erro
	return resposta, acao_u
# Execucao
resp_sem, u_sem = simular_pid_pratico(anti_windup=False)
resp_com, u_com = simular_pid_pratico(anti_windup=True)
# --- Plotagem com Ajustes de Escala para Evitar Cortes ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
# Grafico 1: Variavel de Processo (Nivel)
ax1.plot(tempo, resp_sem, label='Sem Anti-Windup (Windup)', color='black', linestyle='--')
ax1.plot(tempo, resp_com, label='Com Anti-Windup (Clamping)', color='black', linestyle='-', linewidth=2)
ax1.axhline(SP, color='black', linestyle=':', label='Setpoint (SP)')
# Ajuste da escala do Nivel: de 0 a 18 para o Setpoint (12) nao ficar no topo
ax1.set_ylim(-1, 18) 
ax1.set_ylabel('Nível h(t)')
ax1.set_title('Impacto do Anti-Windup na Recuperação da Saturação')
ax1.legend(loc='lower right')
ax1.grid(True, alpha=0.3)
# Grafico 2: Sinal de Controle (Esforco do Atuador)
ax2.plot(tempo, u_sem, label='Saída com Windup', color='black', linestyle='--')
ax2.plot(tempo, u_com, label='Saída com Clamping', color='black', linestyle='-', linewidth=1.5)
ax2.axhline(U_MAX, color='black', linestyle='-.', label='Limite de Saturação (U_MAX)')
# Ajuste da escala do Controle: de -2 a 13 para aparecer a curva e o limite (10) claramente
ax2.set_ylim(-2, 13) 
ax2.set_ylabel('Sinal de Controle u(t)')
ax2.set_xlabel('Tempo (s)')
ax2.legend(loc='lower right')
ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

