"""

6.5.1 Integrais indefinidas. - pág. 160-161

"""
from sympy import symbols, integrate

x = symbols('x')
f = 3*x**2 + 4*x + 1

F = integrate(f, x)

print(F)

