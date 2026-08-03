"""

6.7.4 Visualidade da Aproximação. - pág. 178

"""
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')
f = sp.exp(-x)

# Aproximações de 1ª (linear) e 2ª ordem (quadrática)
f_lin = f.series(x, 0, 2).removeO()
f_quad = f.series(x, 0, 3).removeO()

# Convertendo expressões simbólicas em funções numéricas
f_num = sp.lambdify(x, f, 'numpy')
f_lin_num = sp.lambdify(x, f_lin, 'numpy')
f_quad_num = sp.lambdify(x, f_quad, 'numpy')

# Criando o gráfico
x_vals = np.linspace(-1, 1, 200)

plt.figure(figsize=(7,4))

plt.plot(x_vals, f_num(x_vals),
color='black', linewidth=2,
label='Real: $e^{-x}$')

plt.plot(x_vals, f_lin_num(x_vals),
linestyle='--', color='black', linewidth=1.6,
label='Linear (1ª ordem)')

"""
Explicação importante:

1) x_vals = np.linspace(-1, 1, 200)
   Cria um array NumPy com 200 valores igualmente espaçados entre -1 e 1.
   Exemplo: [-1.00, -0.99, ..., 0.99, 1.00]

2) f_lin_num = lambdify(x, f_lin, 'numpy')
   O lambdify converte a expressão simbólica f_lin (SymPy)
   em uma função numérica compatível com NumPy.
   Ou seja, f_lin_num passa a ser uma função que aceita arrays.

3) f_lin_num(x_vals)
   Avalia a função aproximada f_lin em TODOS os pontos do vetor x_vals.
   É exatamente como calcular y = f(x), só que para vários valores ao mesmo tempo.

Resumo:
lambdify transforma f(x) simbólico → função NumPy.
x_vals é o domínio numérico.
f_lin_num(x_vals) produz os valores da série de Taylor nesse domínio.
"""


plt.plot(x_vals, f_quad_num(x_vals),
linestyle=':', color='black', linewidth=1.6,
label='Quadrática (2ª ordem)')

plt.grid(True, color='gray', linestyle=':', linewidth=0.7)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Validade da Série de Taylor em torno de x = 0")
plt.legend()
plt.tight_layout()
plt.show()