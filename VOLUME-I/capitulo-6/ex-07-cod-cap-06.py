"""

Exemplo adicional: derivada de uma função trigonométrica composta.  -  pág.149

"""
import sympy as sp

t = sp.symbols('t')

g = sp.sin(3*t**2)
dg_dt = sp.diff(g, t)

print("g(t) = ", g)
print("g'(t) = ", dg_dt)

