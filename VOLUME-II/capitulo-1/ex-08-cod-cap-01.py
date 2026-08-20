# -*- coding: utf-8 -*-
"""



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

def simular_pid(Kp, Ki, Kd):
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

        # 3. Perturbacao em t = 20s
        disturbio = 1.5 if t > 20 else 0.0

        # 4. Dinamica do processo
        h_ddot = (u + disturbio) - a*h_dot - b*h

        # 5. Integracao numerica (Euler)
        h_dot = h_dot + h_ddot * dt
        h = h + h_dot * dt

        resposta.append(h)
        erro_anterior = erro

    return resposta

# --- SUBSTITUIR O BLOCO DE EXECUÇÃO FINAL DO CÓDIGO 8 POR ESTE ---

# 1. Resposta com sintonia original (estável)
resp_estavel = simular_pid(Kp=2.0, Ki=0.15, Kd=2.5)

# 2. Resposta com Ki elevado (instável)
resp_agressiva = simular_pid(Kp=2.0, Ki=2.0, Kd=2.5)

# 3. Geracao do grafico comparativo
plt.figure(figsize=(10, 5))
plt.plot(tempo, resp_estavel, label='PID Original (Estável)',
         linestyle='-', color='black')
plt.plot(tempo, resp_agressiva, label='PID Ki=2.0 (Instável)',
         linestyle='--', color='black')

plt.axhline(SP, color='k', linestyle=':', label='Setpoint')

plt.xlabel('Tempo (s)')
plt.ylabel('h(t)')
plt.title('Efeito do Excesso de Ganho Integral no Controle PID')
plt.legend()
plt.grid(True)
plt.show()
