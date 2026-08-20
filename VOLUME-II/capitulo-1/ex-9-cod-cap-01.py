# -*- coding: utf-8 -*-
"""

1.7.1 Exemplo Prático: Análise de Desempenho e Rejeição de Perturbação. - pág.28

"""
import numpy as np
import matplotlib.pyplot as plt

# Configurações de simulação
SP = 6.0
dt = 0.05
tempo = np.arange(0, 60, dt)

# Parâmetros do processo (Modelo de Segunda Ordem)
# Dinâmica: h'' + a*h' + b*h = u + dist
a, b = 0.5, 0.2

def simular_desempenho(Kp, Ki, Kd):
    h, h_dot = 0.0, 0.0
    erro_anterior = SP - h
    integral_erro = 0.0
    resposta = []

    for t in tempo:
        # 1. Erro e componentes PID
        erro = SP - h
        integral_erro += erro * dt
        dedt = (erro - erro_anterior) / dt

        # 2. Lei PID
        u = Kp * erro + Ki * integral_erro + Kd * dedt

        # 3. Perturbação em t = 20 s
        dist = 1.5 if t > 20 else 0.0

        # 4. Dinâmica do processo
        h_ddot = (u + dist) - a*h_dot - b*h
        h_dot = h_dot + h_ddot * dt
        h = h + h_dot * dt

        resposta.append(h)
        erro_anterior = erro

    return resposta

# Simulação com uma sintonia fixa (exemplo didático)
resp = simular_desempenho(Kp=2.5, Ki=0.2, Kd=3.0)

# Plotagem
plt.figure(figsize=(10, 6))
plt.plot(tempo, resp, color='black', linewidth=2, label='Resposta do Sistema')
plt.axhline(SP, color='black', linestyle='-.', alpha=0.7, label='Setpoint')
plt.axvline(20, color='black', linestyle='-', alpha=0.2)
plt.text(21, 5.2, 'Início da Perturbação', fontsize=10, weight='bold')

plt.title('Análise de Desempenho e Rejeição de Perturbação')
plt.xlabel('Tempo (s)')
plt.ylabel('Nível h(t)')
plt.legend(loc='lower right')
plt.grid(True, alpha=0.3)
plt.show()
