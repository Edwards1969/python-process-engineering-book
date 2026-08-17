# -*- coding: utf-8 -*-
"""

5.10 Estudo de Caso: Controle PID em um Forno Industrial Realista. pág.329

"""
import numpy as np
import matplotlib.pyplot as plt

def simular_forno_industrial(setpoint, T_inicial, Kp, Ki, Kd, tempo_total):
	# --- Parâmetros Físicos do Forno ---
	tau = 25.0          # Inércia térmica (constante de tempo)
	T_amb = 25.0        # Temperatura ambiente
	T_max_ganho = 400.0 # Temperatura máxima teórica (u=100%)
    
	# --- Configurações de Simulação ---
	dt = 1.0
	tempos = np.arange(0, tempo_total, dt)
	T_real = T_inicial
	T_sensor = T_inicial # Temperatura "sentida" pelo sensor (com atraso)
	erro_anterior = 0
	integral = 0
	historico_T = []
	historico_u = []
    
	for t in tempos:
		# 1. O SENSOR (Simulando ruído de leitura de +/- 0.5 graus)
		T_medida = T_sensor + np.random.normal(0, 0.5)
        
		# 2. CÁLCULO DO ERRO
		erro = setpoint - T_medida
        
		# 3. CONTROLADOR PID (Algoritmo Digital)
		proporcional = Kp * erro
		integral += erro * Ki * dt
		derivativo = (erro - erro_anterior) * Kd / dt
		u_calculado = proporcional + integral + derivativo
        
		# 4. SATURAÇÃO E ANTI-WINDUP
        
		# O atuador real só opera entre 0.0 (0%) e 1.0 (100%)
		u_sat = max(0.0, min(1.0, u_calculado))
        
		# Lógica Anti-windup: interrompe a integral se o atuador travar no limite
		if u_calculado != u_sat:
			integral -= erro * Ki * dt
		u = u_sat
        
		# 5. DINÂMICA DA PLANTA (Equação de troca térmica)
        
		# dT depende da potência aplicada menos a perda para o ambiente
		dT = ((T_max_ganho * u) - (T_real - T_amb)) * dt / tau
		T_real += dT
        
		# Atualização da inércia do sensor (atraso dinâmico de leitura)
		T_sensor += (T_real - T_sensor) * 0.4
        
		# Armazenamento de dados
		historico_T.append(T_real)
		historico_u.append(u * 100) # Convertendo para porcentagem
		erro_anterior = erro
	return tempos, historico_T, historico_u

# --- Parâmetros de Entrada ---
setpoint = 300
temperatura_inicial = 200

# Sintonização sugerida para sistemas térmicos lentos
Kp, Ki, Kd = 0.06, 0.003, 0.02
tempo_total = 400

# Execução da Simulação
tempos, temps, potencias = simular_forno_industrial(
setpoint, temperatura_inicial, Kp, Ki, Kd, tempo_total
)

# --- Geração dos Gráficos Comparativos ---

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Gráfico de Temperatura
ax1.plot(tempos, temps, label='Temperatura Real do Forno', color='black', lw=2)
ax1.axhline(y=setpoint, color='gray', linestyle='--', label='Setpoint (Desejado)')
ax1.set_ylabel('Temperatura [°C]')
ax1.set_title('Simulação de Controle de Temperatura PID - Forno Industrial')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Gráfico de Esforço de Controle
ax2.fill_between(tempos, potencias, color='silver', alpha=0.5, label='Potência da Resistência (%)')
ax2.set_ylabel('Ação de Controle [u%]')
ax2.set_xlabel('Tempo [s]')
ax2.set_ylim(-5, 105)
ax2.legend()
ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

