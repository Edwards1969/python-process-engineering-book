# -*- coding: utf-8 -*-
"""

1.2.2 Análise de Sistemas de Segunda Ordem sob Controle Proporcional. - pág. 7

"""
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do processo (Segunda Ordem)
a = 0.6     # Coeficiente de amortecimento (atrito/viscosidade)
b = 0.1     # Coeficiente de rigidez (tendência de retorno)

# Parâmetros de Simulação
SP = 6.0    # Setpoint
dt = 0.05   # Passo de tempo
tempo = np.arange(0, 40, dt)

def simular(kc):
    h = 2.0      # Posição (nível) inicial
    h_dot = 0.0  # Velocidade inicial
    resposta = []
    for t in tempo:
        # 1. Cálculo do Erro
        erro = SP - h
        
        # 2. Ação de Controle Proporcional
        u = kc * erro
        
        # 3. Equação Diferencialde 2^a Ordem (Aceleração)
        # h_ddot = u - a*h_dot - b*h
        h_ddot = u - a* h_dot - b*h
        
        # 4. Atualiza velocidade
        h_dot = h_dot + h_ddot * dt
        
        # Atualiza posição
        h = h+ h_dot * dt
        resposta.append(h)
    return resposta

# Configuração de Ganhos para comparação
kc1, kc2, kc3 = 1.0, 2.0, 3.5
resp1 = simular(kc1)
resp2 = simular(kc2)
resp3 = simular(kc3)

# Plotagem Monocromática com Marcadores para Impressão.
plt.figure(figsize=(10, 5))
plt.plot(tempo, resp1, color='black', linestyle='-',  label=r'$k_{c1}$ (baixo ganho)')
plt.plot(tempo, resp2, color='black', linestyle='--', label=r'$k_{c2}$ (médio ganho)')
plt.plot(tempo, resp3, color='black', linestyle=':',  label=r'$k_{c3}$ (alto ganho)')

plt.axhline(SP, color='black', linestyle='-.', alpha=0.7, label='Setpoint')    
plt.xlabel('Tempo (s)')
plt.ylabel('h(t)')
plt.title('Resposta o Processo de $2^a$ Ordem com Controle Proporcional')
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

















