"""

7.5.1 Resolução Computacional com SymPy. - pág 202

"""

import sympy as sp


# DEfinição a matriz e o vetor simbolicamente.
A = sp.Matrix([
	[2,1],
	[0,3]
	])

x = sp.Matrix([4,5])

# Realizando o produto.
y = A * x

print("Matriz A: \n")
sp.pprint(A)

print("\nVetor x: \n")
sp.pprint(x)

print("\nResulado Ax: \n")
sp.pprint(y)