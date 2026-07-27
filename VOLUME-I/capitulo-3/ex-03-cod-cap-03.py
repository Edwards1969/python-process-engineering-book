"""
3.4.1 Operações matemáticas elementares - pág.51
"""
import numpy as np

x = np.array([0, 1, 2, 3])

print(np.exp(x))
print(np.sqrt(x))
print(np.sin(x))

"""
3.4.2 Operações estatísticas - pág: 52
"""
dados = np.array([10, 12, 15, 20, 18])

print(np.mean(dados))
print(np.std(dados))
print(np.min(dados), np.max(dados))

"""
3.4.3 Operações agregadas em matrizes
"""

M = np.array([
    [1, 2, 3], 
    [4, 5, 6]
    ])

print(np.mean(M, axis=0))   # média por coluna
print(np.mean(M, axis=1))   # média por linha

"""

"""

