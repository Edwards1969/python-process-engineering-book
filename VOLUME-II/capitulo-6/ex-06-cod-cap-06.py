# -*- coding: utf-8 -*-
"""

6.8 Modelo Térmico Contínuo e Simulação Alternativa. - pág. 356

"""
import numpy as np
import pandas as pd

dt = 1.0
tempo = np.arange(0, 3000, dt)

# --------------------------
# Parâmetros do forno
# --------------------------
Tmax = 450
tau_forno = 80
T = np.zeros_like(tempo, dtype=float)
T[0] = 25
Tset = 350

# --------------------------
# PID
# --------------------------
Kp = 6.0
Ki = 0.05
Kd = 20.0
erro_anterior = 0
integral = 0

# --------------------------
# Sensor com atraso
# --------------------------
tau_sensor = 20
T_sensor = np.zeros_like(T)
ruido = np.random.normal(0, 0.5, len(T))

# --------------------------
# Perturbação térmica
# --------------------------
perturbacao = np.zeros_like(T)

historico = []

for i in range(1, len(tempo)):

    # Simulação de abertura da porta
    if 1200 <= tempo[i] <= 1300:
        perturbacao[i] = -3.5

    # Sensor com atraso
    T_sensor[i] = (
        T_sensor[i-1]
        + (T[i-1] - T_sensor[i-1]) / tau_sensor
    )

    T_medida = T_sensor[i] + ruido[i]

    # Erro
    erro = Tset - T_medida

    # Integral
    integral += erro * dt

    # Derivada
    derivada = (erro - erro_anterior) / dt

    # PID bruto
    u = Kp*erro + Ki*integral + Kd*derivada

    # Saturação
    u_sat = max(0, min(1, u))

    # Anti-windup (clamping)
    if u != u_sat:
        integral -= erro * dt

    u = u_sat

    # Dinâmica do forno
    T[i] = (
        T[i-1]
        + (Tmax*u - T[i-1]) * dt / tau_forno
        + perturbacao[i]
    )

    erro_anterior = erro

    historico.append([
        tempo[i],
        T[i],
        T_medida,
        u
    ])

tabela_forno = pd.DataFrame(
    historico,
    columns=[
        "tempo_s",
        "T_processo_C",
        "T_medida_C",
        "u"
    ]
)

"""

6.8.1 Métricas de Desempenho. - pág.358

"""
erro = Tset - tabela_forno["T_processo_C"]
IAE = np.sum(np.abs(erro)) * dt
ISE = np.sum(erro**2) * dt
overshoot = (
tabela_forno["T_processo_C"].max()
- Tset
)
print("IAE:", IAE)
print("ISE:", ISE)
print("Overshoot (°C):", overshoot)


"""

6.8.2 Análise Gráfica. - pág. 359 

"""
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
plt.plot(tabela_forno["tempo_s"],
	tabela_forno["T_processo_C"],
	label="Temperatura do Forno")
plt.plot(tabela_forno["tempo_s"],
	tabela_forno["T_medida_C"],
	label="Temperatura Medida",
	alpha=0.7)
plt.axhline(Tset,
	color="red",
	linestyle="--",
	label="Setpoint")
plt.xlabel("Tempo (s)")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)
plt.show()
plt.figure(figsize=(10,4))
plt.plot(tabela_forno["tempo_s"],
	tabela_forno["u"],
	label="Potência Aplicada (u)")
plt.xlabel("Tempo (s)")
plt.ylabel("Potência Normalizada")
plt.grid(True)
plt.show()

"""

6.8.2 Análise Gráfica

"""
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
plt.plot(tabela_forno["tempo_s"],
	tabela_forno["T_processo_C"],
	label="Temperatura do Forno")
plt.plot(tabela_forno["tempo_s"],
	tabela_forno["T_medida_C"],
	label="Temperatura Medida",
	alpha=0.7)
plt.axhline(Tset,
	color="red",
	linestyle="--",
	label="Setpoint")
plt.xlabel("Tempo (s)")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)
plt.show()
plt.figure(figsize=(10,4))
plt.plot(tabela_forno["tempo_s"],
	tabela_forno["u"],
	label="Potência Aplicada (u)")
plt.xlabel("Tempo (s)")
plt.ylabel("Potência Normalizada")
plt.grid(True)
plt.show()
































