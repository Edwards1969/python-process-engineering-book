"""

7.8.5 Estabilidade de Sistemas de Controle.  -  pág. 212

"""
import numpy as np

# Matriz de um sistema de segunda ordem amortecdo.
A_controle = np.array([
	[0, 1], 
	[-5, -2]
	])

autovals, _ = np.linalg.eig(A_controle)

print(f"Autovalores do Sistema: {autovals}")
# Parte real negativa indica estabilidade.