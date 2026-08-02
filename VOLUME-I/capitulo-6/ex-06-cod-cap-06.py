"""

6.3.6 Derivadas de Funções Compostas.  -  pág. 147

"""
import sympy as sp

t = sp.symbols('t')

f = t*sp.exp(2*t)
df_dt = sp.diff(f, t)

print("f(t) = ", f)
print("f'(t) = ", df_dt)

