"""

6.3.3 Derivadas em Múltiplas Variáveis. - pág.142

Exempo: Derivada parcial de uma função escalar

"""
import sympy as sp

# Variáveis simbólicas.
x, y, z = sp.symbols('x y z')

# Função escalar.
f = x**2 * y + 3*y*z - sp.sin(z)

# Derivadas parciais.
df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)
df_dz = sp.diff(f, z)

print("df/dx = ", df_dx)
print("df/dz = ", df_dy)
print("df/dz = ", df_dz)
