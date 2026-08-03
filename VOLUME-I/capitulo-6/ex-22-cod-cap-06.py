"""

6.7.6 Exercício Resolvido: Linearizaçõ de um Sistema Térmico. - pág. 181

"""
import sympy as sp

sigma, T, T0 = sp.symbols('sigma T T0')
fluxo = sigma * T**4

# Expansão de 1^a ordem em torno de T0.
linearizacao = fluxo.series(T, T0, 2).removeO()

print(f"Modelo Linear: {linearizacao}")