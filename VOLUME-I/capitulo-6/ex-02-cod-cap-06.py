"""

6.3.3 Derivadas em Múltiplas Variáveis. - pág.140

Exempo: Função vetorial de posição.

"""
import sympy as sp

# Variável temporal.
t = sp.symbols('t')

# Componente da posição.
x = t**2
y = 3*t + 1
z = sp.sin(t)

# Vetor posição.
r = sp.Matrix([x, y, z])

# Derivada componente a componente.
v = r.diff(t)

print("Vetor velocidade v(t) = ")
print(v)
 

