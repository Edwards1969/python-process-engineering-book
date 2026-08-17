# -*- coding: utf-8 -*-
"""

5.7.4 — Integração com Sensor e Controle PID (Malha Fechada) pág. 308

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Passo de tempo
dt = 0.1
tempo = np.arange(0, 200, dt)

# Parâmetros do processo
Tmax = 300
tau = 25

# Parâmetros PID
Kp = 0.02
Ki = 0.001
Kd = 0.1
Tref = 150

# Variáveis internas
u = 0
erro_anterior = 0
integral = 0

# Vetores de temperatura
T = np.zeros_like(tempo)
T_sensor = np.zeros_like(tempo)

# Condições iniciais
T[0] = 25
T_sensor[0] = 25

# Atraso térmico do sensor
tau_sensor = 8

# Loop PID
for i in range(1, len(tempo)):
    # Sensor com atraso
    T_sensor[i] = T_sensor[i-1] + (T[i-1] - T_sensor[i-1]) / tau_sensor

    # Erro
    erro = Tref - T_sensor[i]

    # PID
    integral += erro * dt
    derivada = (erro - erro_anterior) / dt
    u = Kp*erro + Ki*integral + Kd*derivada

    # Saturação
    u = max(0, min(1, u))

    # Processo térmico
    T_fonte = Tmax * u
    T[i] = T[i-1] + (T_fonte - T[i-1]) * dt / tau

    erro_anterior = erro

# Tabela final
tabela_malha_fechada = pd.DataFrame({
    "tempo_s": tempo,
    "T_processo_C": T,
    "T_sensor_C": T_sensor
})

# Gráfico
plt.figure(figsize=(10,5))

plt.plot(tempo, T, linestyle='-', color='black', label='Temperatura do Processo')
plt.plot(tempo, T_sensor, linestyle='--', color='black', label='Temperatura do Sensor')
plt.axhline(Tref, linestyle=':', color='black', linewidth=2, label='Setpoint')

plt.xlabel("Tempo (s)")
plt.ylabel("Temperatura (°C)")
plt.title("Resposta em Malha Fechada do Sistema Térmico")
plt.legend()
plt.grid(True)
plt.show()

"""

5.7.6 Integração com Sensor Simulado. pág. 312

"""
#Integração com Sensores Simulado
# Agora combinamos o processo térmico com o modelo de termopar 
# apresentado anteriormente.

# Atraso térmico do sensor.
tau_sensor = 12
T_sensor = np.zeros_like(T)

for i in range(1, len(T)):
    T_sensor[i] = T_sensor[i-1] + (T[i] - T_sensor[i-1])/tau_sensor

# Ruído térmico (C)
ruido = np.random.normal(0, 0.2, len(T))

# Temperatar medida com ruído
T_sensor_ruidoso = T_sensor + ruido

# Tensão do termopar (mV)
S = 0.041
E_mV = S * T_sensor_ruidoso

tabela_sensor = pd.DataFrame({
    "tempo_s": tempo,
    "T_processo_C": T,
    "T_sensor_C": T_sensor_ruidoso,
    "Tensao_mV": E_mV
})

tabela_sensor

"""

5.7.7 Filtragem Digital do Sinal do Sensor. pág. 313

"""


alpha = 0.85
T_filtrado = np.zeros_like(T_sensor_ruidoso)

for i in range(1, len(T_sensor_ruidoso)):
    T_filtrado[i] = ( 
        alpha * T_filtrado[i-1] +
        (1 - alpha) * T_sensor_ruidoso[i]
        )

tabela_sensor["T_filtrado_C"] = T_filtrado

tabela_sensor



















