"""

7.6.1 Transposição de Matrizes. - pág. 203

"""
import numpy as np

A = np.array([
	[3,1],
	[2,4]
	])

print("Matriz A \n = ", A)

# Na matriz transposição o que era linha vira coluna.

print("Matriz Transposição \n = ", A.T)