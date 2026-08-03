"""

6.7.1 Implementação Simbólica com SymPy.  -  pág. 176-177

"""
from sympy import symbols, exp, sin

x = symbols('x')
f = exp(x)

# Expansão em torno de x=0 (Série de Maclaurin) até a ordem 5
serie_exp = f.series(x, 0, 5)

# O método removeO() retira o termo de erro
polinomio = serie_exp.removeO()

print(f"Serie com erro: {serie_exp}")

# Confira se chegou nesses resultados:
# Serie com erro: 1 + x + x**2/2 + x**3/6 + x**4/24 + O(x**5)
# Polinomio puro: x**4/24 + x**3/6 + x**2/2 + x + 1
