"""

6.3.1 Derivadas Simples.  -  pág.138

"""
from sympy import symbols, diff

# Variável temporal.
t = symbols('t')

# Função de posição.
x = 5*t**2 + 3*t + 2

# Derivada simbólica (velocidade).
dx = diff(x, t)

print("Derivada da função x(t): ", dx)