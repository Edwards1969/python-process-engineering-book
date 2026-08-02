"""

Exemplo adicional: derivada de uma função logarítmica composta. - pág.151

"""
import sympy as sp

t = sp.symbols('t')

h = sp.log(5*t**3 + 1)
dh_dt = sp.diff(h, t)

print("h(t) = ", h)
print("h'(t) = ", dh_dt)
