""""

6.3.4 Derivadas Parciais.  -  pág. 145

"""
import sympy as sp

x, y = sp.symbols('x y')
T = 3*x**2 + 2*x*y + y**3

dT_dx = sp.diff(T, x)
dT_dy = sp.diff(T, y)

print("dT/dx = ", dT_dx)
print("dT/dy = ", dT_dy)




