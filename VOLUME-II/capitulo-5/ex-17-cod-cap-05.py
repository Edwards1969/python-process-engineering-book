# -*- coding: utf-8 -*-
"""

5.8 Controle PID de Temperatura. - pág. 314

5.8.5 Implementação Computacional Completa. - pág. 314

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============================
# Simulação do processo térmico
# ============================
dt = 1.0
tempo = np.arange(0, 1000, dt)

# Parâmetros do processo
Tmax = 300
tau = 30
T = np.zeros_like(tempo, dtype=float)
T[0] = 25

# PID
kp = 0.02
ki = 0.001
kd = 0.1
setpoint = 150
erro_anterior = 0
integral = 0

# Vetores auxiliares
u = np.zeros_like(tempo)
perturbacao = np.zeros_like(tempo)

for k in range(1, len(tempo)):
	# Perturbação externa (abertura da porta)
	if 400 <= k <= 450:
		perturbacao[k] = -0.8   # perda de calor
        
	# Erro
	erro = setpoint - T[k-1]
    
	# Integral
	integral += erro * dt
    
	# Derivativo
	derivativo = (erro - erro_anterior) / dt
    
	# PID
	u[k] = kp*erro + ki*integral + kd*derivativo
    
	# Saturação
	if u[k] > 1:
		u[k] = 1
		integral -= erro * dt
	elif u[k] < 0:
		u[k] = 0
		integral -= erro * dt
        
	# Processo térmico
	T_fonte = Tmax * u[k]
	T[k] = (
		T[k-1]
		+ (T_fonte - T[k-1]) * dt / tau
		+ perturbacao[k]
	)
	erro_anterior = erro
    
# ============================
# Criação da tabela
# ============================
tabela_pid = pd.DataFrame({
	"tempo_s": tempo,
	"Temperatura_C": T,
	"Controle_u": u,
	"Perturbacao": perturbacao
})

# ============================
# Gráficos
# ============================
plt.figure(figsize=(12, 8))

# --- Gráfico 1: Temperatura ---
plt.subplot(2, 1, 1)
plt.plot(tempo, T, label="Temperatura (°C)", linewidth=2)
plt.axhline(setpoint, color='black', linestyle='--', label="Setpoint")
plt.fill_between(tempo, min(T)-5, max(T)+5,
where=(tempo >= 400) & (tempo <= 450),
color='black', alpha=0.2, label="Perturbação")
plt.ylabel("Temperatura (°C)")
plt.title("Resposta do Processo Térmico com Controle PID e Perturbação")
plt.grid(True)
plt.legend()

# --- Gráfico 2: Controle e Perturbação ---
plt.subplot(2, 1, 2)
plt.plot(tempo, u, label="Sinal de Controle u(t)", linewidth=2)
plt.plot(tempo, perturbacao, label="Perturbação Q(t)", linewidth=2)
plt.xlabel("Tempo (s)")
plt.ylabel("u(t) e Q(t)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


