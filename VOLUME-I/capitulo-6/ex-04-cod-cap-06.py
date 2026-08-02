"""

6.3.4 Aplicação em Engenharia: velocidade e aceleração. -  pág.143

"""
import sympy as sp

t = sp.symbols('t')

# Função posição.
s = 4*t**3 - 2*t**2 + 7*t

# Derivadas sucessivas.
v = sp.diff(s, t)     # velocidade
a = sp.diff(v, t )    # aceleração

print("v(t) = ", v)
print("a(t) = ", a)