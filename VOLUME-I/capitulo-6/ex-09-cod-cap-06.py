"""

6.3.7 Derivada de ordem superior. -pág. 153

"""
import sympy as sp

t = sp.symbols('t')
x = 5*t**4 - 3*t**2 + 2*t

segunda = sp.diff(x, t, 2)
terceira =  sp.diff(x, t, 3)

print("x''(t) = ", segunda)
print("x'''(t) = ", terceira)


