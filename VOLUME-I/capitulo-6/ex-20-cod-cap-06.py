"""

6.7.3 Aplicação na Instrumentação: Linearização de Sensores.  -  pág. 177-178 

"""
from sympy import symbols, sqrt

h, ho = symbols('h ho')
Q = sqrt(h)

# Ponto de operação.
ponto_op = 4

# Linearização: Sirie de Taylor até a 1a ordem (n=2 no SymPy).
Q_linear = Q.series(h, ponto_op, 2).removeO()

print(f"Equação linearizada em h = 4, Q(h) = {Q_linear}")

