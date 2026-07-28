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
3.4.3 Operações agregadas em matrizes pág. 52

"""

M = np.array([
    [1, 2, 3], 
    [4, 5, 6]
    ])

print(np.mean(M, axis=0))   # média por coluna
print(np.mean(M, axis=1))   # média por linha

"""
3.4.4 Normas e operações vetoriais - pág 52

"""
v = np.array([3,4])

norma = np.linalg.norm(v)

print(norma)

"""
3.4.5 Aplicação em Engenharia: cálculo de tensão média - pág 53

"""
sigma = np.array([120, 130, 128, 140, 135])

media = np.mean(sigma)
desvio = np.std(sigma)

print("Tensão média: ", media)
print("Densidade padrão: ", desvio)

"""
3.4.6 Aplicação em Engenharia: decaimento exponencial - pág 53

"""
t = np.linspace(0, 10, 100)

k = 0.3
T0 = 80
Ta = 25

T = Ta + (T0 - Ta)*np.exp(-k*t)

print("Temperatura: ", T)
