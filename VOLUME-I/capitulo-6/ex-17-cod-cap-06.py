# -*- coding: utf-8 -*-
"""

6.6.2 Parte 2: Processamento Numérico com SciPy.  -  pág. 174

Exemplo: processamento de dados reais de um sensor.

"""
import numpy as np
import matplotlib.pyplot as plt

# Dados simulados do sensor (Pressão em Pascals)
pressao = np.array([50000, 48000, 45000, 40000, 32000, 25000, 15000, 5000])
tempo = np.arange(0, 8, 1) # horas

# Parâmetrosdo fluido e do tanque.
rho = 1000 # densidade da água (Kg/m3)
g = 9.81   # gravidade (m/s2)
R_tanque = 2.0
H_tanque = 6.0

# 1. Converter pressão em altura (h = p / (rho * g))
alturas = pressao / (rho * g)

# 2. Calcular o Volume em daeda ponto usand a fórmula obtida o SymPy.
volumes = (np.pi*R_tanque**2 * alturas**3) / (3 * H_tanque**2) 

# 3. Calcular a vazão média entre os intervalos (Derivada Numérica)
vazao = -np.diff(volumes)/ np.diff(tempo)

"""
Observação:
    
Como a pressão diminui ao longo do tempo, a altura e o volume também diminuem.
Isso faz com que ΔV seja negativo. Para que a vazão de saída seja positiva,
usamos o sinal de menos na expressão: vazão = -ΔV/Δt.

    pressão ↓ → altura ↓ → volume ↓ → derivada negativa

"""

print("-------------------------------------------------------------------------")
print(f"Volumes calculados (m3): {volumes}" )
print("-------------------------------------------------------------------------")
print(f"Vazão média de saída (m3/h): {vazao}" )
print("-------------------------------------------------------------------------")


# 4. Plotar a vazão média por intervalo de tempo
tempo_vazao = tempo[1:]  # ajustar o vetor de tempo para combinar com np.diff

plt.plot(tempo_vazao, vazao, marker='o')
plt.xlabel("Tempo (h)")
plt.ylabel("Vazão média (m³/h)")
plt.title("Vazão Média por Intervalo de Tempo")
plt.grid(True)
plt.tight_layout()
plt.show()



