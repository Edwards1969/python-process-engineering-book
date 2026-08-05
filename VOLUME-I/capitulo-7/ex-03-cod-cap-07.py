"""

7.7.1 Exemplo Real: Equilíbrio Estático em uma Estrutura.  -  pág. 207

"""
import numpy as np

A = np.array([
	[3, 1], 
	[2, 4]
	])
b = np.array([20, 30])

# Uso do solver otimizado.
reacoes = np.linalg.solve(A, b)

print(f"R1 = {reacoes[0]:.2f} N")
print(f"R2 = {reacoes[1]:.2f} N")
