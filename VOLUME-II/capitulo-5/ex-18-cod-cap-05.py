# -*- coding: utf-8 -*-
"""

5.9 Integração Sensor + Modelo Térmico + Controle PID. - pág. 321

5.9.4 Simulação Computacional Completa - pág. 324

"""
import numpy as np
import matplotlib.pyplot as plt

def simular_controle(Kp, Ki, Kd, Tset, tempo, dt):
	# Parâmetros da Planta
	Tmax, tau = 300, 45
	T = np.zeros_like(tempo)
	T[0] = 25
    
	# Sensor e Controle
	tau_sensor = 15
	T_sensor = np.zeros_like(T)
	T_sensor[0] = 25
	u_hist = np.zeros_like(tempo)
	erro_anterior = 0
	integral = 0
    
	for i in range(1, len(tempo)):
		# Perturbação (Porta aberta)
		perturbacao = -2.5 if 600 <= tempo[i] <= 650 else 0
        
		# Modelo do Sensor (Atraso + Ruído)
		T_sensor[i] = T_sensor[i-1] + (T[i-1] - T_sensor[i-1]) * dt / tau_sensor
		T_medida = T_sensor[i] + np.random.normal(0, 0.2)
        
		# PID
		erro = Tset - T_medida
		integral += erro * dt
		derivada = (erro - erro_anterior) / dt
		u = Kp*erro + Ki*integral + Kd*derivada
		u_sat = max(0, min(1, u))
        
		# Anti-windup
		if u != u_sat:
			integral -= erro * dt
		u = u_sat
		u_hist[i] = u
        
		# Planta
		T[i] = T[i-1] + (Tmax*u - T[i-1]) * dt / tau + perturbacao
		erro_anterior = erro
	return T, u_hist

# Configurações globais
dt = 1.0
tempo = np.arange(0, 1200, dt)
Tset = 180

# Cenário 1: MAL AJUSTADO (Oscilatório)
T1, u1 = simular_controle(Kp=10.0, Ki=0.20, Kd=25.0,
Tset=Tset, tempo=tempo, dt=dt)

# Cenário 2: AJUSTADO (Estável)
T2, u2 = simular_controle(Kp=1.2, Ki=0.020, Kd=0.8,
Tset=Tset, tempo=tempo, dt=dt)

# --- GERAÇÃO DOS GRÁFICOS DIDÁTICOS ---

fig, ax = plt.subplots(2, 2, figsize=(14, 10), sharex=True)

# Plot 1: Temperatura Mal Ajustada
ax[0,0].plot(tempo, T1, color='black', label='Temperatura Real')
ax[0,0].axhline(y=Tset, color='black', linestyle=':', label='Setpoint')
ax[0,0].set_title("Sintonia Mal Ajustada (Oscilatória)")
ax[0,0].set_ylabel("Temperatura (°C)")
ax[0,0].legend()

# Plot 2: Ação de Controle Mal Ajustada
ax[1,0].step(tempo, u1, color='black', alpha=0.7)
ax[1,0].set_ylabel("Ação de Controle (u)")
ax[1,0].set_xlabel("Tempo (s)")

# Plot 3: Temperatura Ajustada
ax[0,1].plot(tempo, T2, color='black', label='Temperatura Real')
ax[0,1].axhline(y=Tset, color='black', linestyle=':', label='Setpoint')
ax[0,1].set_title("Sintonia Ajustada (Estável)")
ax[0,1].legend()

# Plot 4: Ação de Controle Ajustada
ax[1,1].step(tempo, u2, color='black', alpha=0.7)
ax[1,1].set_xlabel("Tempo (s)")
for a in ax.flat:
	a.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

"""

5.9.6 Filtragem Digital. - 327 

"""

def simular_controle(Kp, Ki, Kd, Tset, tempo, dt):
    Tmax, tau = 300, 45
    T = np.zeros_like(tempo)
    T[0] = 25

    tau_sensor = 15
    T_sensor = np.zeros_like(T)
    T_sensor[0] = 25

    T_medida = np.zeros_like(T)
    u_hist = np.zeros_like(tempo)

    erro_anterior = 0
    integral = 0

    for i in range(1, len(tempo)):
        perturbacao = -2.5 if 600 <= tempo[i] <= 650 else 0

        # Sensor
        T_sensor[i] = T_sensor[i-1] + (T[i-1] - T_sensor[i-1]) * dt / tau_sensor
        T_medida[i] = T_sensor[i] + np.random.normal(0, 0.2)

        # PID
        erro = Tset - T_medida[i]
        integral += erro * dt
        derivada = (erro - erro_anterior) / dt
        u = Kp*erro + Ki*integral + Kd*derivada
        u_sat = max(0, min(1, u))

        if u != u_sat:
            integral -= erro * dt

        u = u_sat
        u_hist[i] = u

        # Planta
        T[i] = T[i-1] + (Tmax*u - T[i-1]) * dt / tau + perturbacao
        erro_anterior = erro

    return T, T_sensor, T_medida, u_hist

import pandas as pd

# Rodar o cenário AJUSTADO (o que o livro usa para a tabela)
T_real, T_sensor, T_medida, u_hist = simular_controle(
    Kp=1.2, Ki=0.020, Kd=0.8,
    Tset=Tset, tempo=tempo, dt=dt
)

# Criar a tabela PID exatamente como no livro
tabela_pid = pd.DataFrame({
    "tempo_s": tempo,
    "T_processo_C": T_real,
    "T_medida_C": T_medida,
    "u": u_hist
})

# Filtragem digital
alpha = 0.85
T_filtrado = np.zeros_like(tabela_pid["T_medida_C"])

for i in range(1, len(T_filtrado)):
    T_filtrado[i] = (
        alpha*T_filtrado[i-1]
        + (1-alpha)*tabela_pid["T_medida_C"].iloc[i]
    )

tabela_pid["T_filtrada_C"] = T_filtrado

# Imprimir um trecho da tabela no console
print(tabela_pid.head(10))
print(tabela_pid.tail(5))

# Salvar em CSV
tabela_pid.to_csv("tabela_pid.csv", index=False)
print("Arquivo tabela_pid.csv gerado com sucesso!")













