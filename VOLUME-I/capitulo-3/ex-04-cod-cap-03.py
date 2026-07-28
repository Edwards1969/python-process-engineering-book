"""
3.51. Análise de sinais: filtragem simples - pág. 54

"""
import numpy as np

sinal = np.array([10, 12, 15, 14, 50, 16, 15, 14])

janela = 3

media_movel = np.convolve(sinal, np.ones(janela)/janela, mode='valid')
print(media_movel)

"""
3.5.3 Circuitos elétricos: resposta de um RC - pág. 55

"""
import numpy as np

t = np.linspace(0, 5, 100)

R = 2000
C = 1e-6
v0 = 5

v = v0 * (1 - np.exp(-t/(R*C)))

print('A tensão é: ', v)

"""
3.5.4 Transferência de calor: resfriamento de um corpo - pág. 53
"""
import numpy as np

t = np.linspace(0, 200, 200)

T0 = 90
Tamb = 25
k = 0.02

T = Tamb + (T0 - Tamb)*np.exp(-k*t)

print("Temperatura: ", T)

"""
3.3.3 Vibrações mecânicas:  oscilador harmônico - pág 56

"""

import numpy as np

A = 0.05  # m
m = 2.0   # kg
k = 200   # N/m

omega = np.sqrt(k/m)

t = np.linspace(0, 5, 500)

x = A * np.cos(omega * t)

print("Valor e x: ", x)

"""
3.5.6 Métodos  numéricos: derivada aproximada - pág. 56

"""

import numpy as np

x = np.linspace(0, 10, 1000)
h = x[1] - x[0]

f = np.sin(x)

df = (np.sin(x + h) - np.sin(x)) /  h

print("O valor de df: ", df)

"""
3.5.7 Álgebra linear: solução de sistemas. pág: 57

"""

import numpy as np

A = np.array([
    [3, 1],
     [1, 2]
     ])

b = np.array([9, 8])

x = np.linalg.solve(A, b)

print("O valor de x: ", x)