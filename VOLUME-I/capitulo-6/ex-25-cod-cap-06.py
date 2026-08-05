"""

6.7.14 Exercício 5: Energia Armazenada em uma Mola.   -   pág. 188

"""

from sympy import symbols, integrate

x = symbols('x')
k = 150

# A energia é a integral da força (k*x)
energia_acumulada = integrate(k * x, (x, 0, 0.3))

print(f"Energia armazandaa: {energia_acumulada:.4f} Joules")