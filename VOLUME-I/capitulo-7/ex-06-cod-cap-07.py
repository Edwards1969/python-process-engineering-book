"""

7.10.3 - Implementação Computacional com SciPy

"""
import numpy as np
from scipy.linalg import eig

# Definição dos parâmetros físicos.
m1, m2 = 2.0, 1.0
k1, k2, k3 = 6.0, 2.0, 4.0

M = np.array([
	[m1, 0], 
	[0, m2]
	])

k = np.array([
	[k1 + k2, -k2], 
	[-k2, k2 + k3]
	])

# Resolvendo o problema generalizado: k v = lambda M v
vals , vets = eig(k, M)

# Frequências naturais (rad/s)
frequencias = np.sqrt(vals.real)
print("Frequências naturais:")
print(frequencias.reshape(-1, 1))
print("rad/s")


print("\nModos de vibração (Normalizados): ")
modos_norm = vets.real / np.max(np.abs(vets.real), axis=0)
print(modos_norm)