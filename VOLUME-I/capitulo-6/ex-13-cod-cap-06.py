"""

6.5.2 Integrais Definidas. - 162-163

"""
from sympy import symbols, integrate

x = symbols('x')
f = 3*x**2 + 4*x + 1

resultado = integrate(f, (x, 0, 2))
print(f"O valor da integral definida é: {resultado}")

# Cálculo simbólico com limites gerais.
x, a, b = symbols('x a b')
f = 3 * x**2 + 4*x + 1

area = integrate(f, (x, a, b))
print(area)