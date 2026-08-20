# -*- coding: utf-8 -*-
"""

1.10.5 Exemplo Computacional: Controle de Pressão com Filtro Derivativo. - pág.50

"""
import numpy as np
import matplotlib.pyplot as plt
 #--- Parametros do Sistema ---
V, R, T = 10.0, 0.5, 300
dt = 0.05
tempo = np.arange(0, 50, dt)
SP = 20.0
def simular_pressao(Kp, Ki, Kd, filtrar=False):
	P = 15.0 
	Mg = (P * V) / (R * T)
	erro_anterior = SP - P
	integral_erro = 0.0
	u_d_filt = 0.0
	alpha = 0.15 
	res_P = []
	res_U = []
	np.random.seed(10) 
	for t in tempo:
		# Perturbacao de carga em t=15s
		m_in = 3.0 if t < 15 else 7.0
		# Leitura com ruido (Simulando sensor real)
		P_medida = P + np.random.normal(0, 0.1)
		erro = SP - P_medida
		integral_erro += erro * dt
		# Calculo da Derivada
		u_d_pura = Kd * (erro - erro_anterior) / dt
		if filtrar:
			u_d_filt = (1 - alpha) * u_d_filt + alpha * u_d_pura
			u_d = u_d_filt
		else:
			u_d = u_d_pura
		u_calc = Kp * erro + Ki * integral_erro + u_d
		u_final = np.clip(u_calc, 0.5, 15.0) 
		# Dinamica do Processo
		dMg_dt = m_in - u_final
		Mg += dMg_dt * dt
		P = (Mg * R * T) / V
		res_P.append(P)
		res_U.append(u_final)
		erro_anterior = erro
	return res_P, res_U
# Execucao das simulacoes com ganhos bem distintos para visibilidade
# PI configurado com ganho menor para destacar a lentidao
p_pi, u_pi = simular_pressao(Kp=0.6, Ki=0.15, Kd=0.0)
p_ruido, u_ruido = simular_pressao(Kp=1.2, Ki=0.4, Kd=1.8, filtrar=False)
p_limpo, u_limpo = simular_pressao(Kp=1.2, Ki=0.4, Kd=1.8, filtrar=True)
# --- Plotagem Didática com Foco em Impressão ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
# Gráfico 1: Variável de Processo (Pressão)
ax1.plot(tempo, p_pi, label='Controle PI', color='black', linestyle='--', linewidth=1.5)
ax1.plot(tempo, p_ruido, label='PID sem Filtro', color='grey', linestyle=':', linewidth=2)
ax1.plot(tempo, p_limpo, label='PID com Filtro', color='black', linestyle='-', linewidth=2)
ax1.axhline(SP, color='black', linestyle='-.', label='Setpoint', alpha=0.7)
ax1.set_ylabel('Pressão (bar)')
ax1.set_title('Resposta da Pressão em Malha Fechada')
ax1.legend(loc='lower right')
ax1.grid(True, alpha=0.3)
# Gráfico 2: Sinal de Controle (Ação da Válvula)
# Usando marcadores esparsos para diferenciar as linhas de esforço
ax2.plot(tempo, u_pi, label='Saída PI', color='black', linestyle='--', linewidth=1.2)
ax2.plot(tempo, u_ruido, label='Saída PID Ruidosa', color='grey', linestyle=':', linewidth=1)
ax2.plot(tempo, u_limpo, label='Saída PID Suave', color='black', linestyle='-', linewidth=1.5)
ax2.set_ylabel('Abertura da Válvula (u)')
ax2.set_xlabel('Tempo (s)')
ax2.set_title('Esforço do Atuador e Proteção contra Ruído')
ax2.legend(loc='lower right')
ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

