"""

6.7.8 Exercício Resolvido: Linearização de um Sensor de Nível. - pág. 183

"""
import sympy as sp

h = sp.symbols('h')
C = sp.log(h + 1)

# Linearização em torno do ponto h = 5.
# n = 2 gera um polinômio de 1^o Grau (reta)

C_linear = C.series(h, 5, 2).removeO()

print(f"Modelo Linearizado: {C_linear}")

"""
Se o nível subir para 5.1 m?

"""
import sympy as sp

h = sp.symbols('h')
C = sp.log(h + 1)

C_linear = C.series(h, 5, 2).removeO()

# Avaliar em h = 5.1
valor = C_linear.subs(h, 5.1)
print(valor)