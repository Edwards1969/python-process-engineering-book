"""

6.5.3 Aplicação em Engenharia: trabalho de uma força variável. - pág 164-166

"""
from sympy import symbols, integrate

x = symbols('x')
F = 5*x**2 + 2*x

W = integrate(F, (x,0, 3))
print(W,"J")