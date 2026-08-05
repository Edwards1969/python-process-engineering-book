"""

7.8.3 Exemplo Real: Vibrações em um Sistema Massa-Mola.  -  pág.211

"""
import numpy as np
from scipy.linalg import eig

k = np.array([
	[6,-2],
	[-2, 4]
	])

M = np.array([
	[2, 0],
	[0, 1]
	])

# Problema de autovalore generalizado.
valores_p, vetores_p = eig(k, M)

# Frequências naturais (rad/s)
frequencias = np.sqrt(valores_p.real)

"""
Observação sobre o uso de .real:

A função eig() retorna autovalores potencialmente complexos devido a
pequenos erros numéricos dos métodos de álgebra linear. Em sistemas
massa-mola físicos, as frequências naturais devem ser reais.

O atributo .real extrai apenas a parte real dos autovalores, removendo
termos imaginários residuais como 0.j ou valores muito pequenos (ex.: 1e-16j)
que surgem por arredondamento numérico.

Assim, np.sqrt(valores_p.real) garante que estamos calculando frequências
naturais fisicamente válidas.

Exemplo:
z = 3 + 4j
print(z.real)   # 3
print(z.imag)   # 4
"""
print(f"Frequências Naturais: {frequencias} rad/s")
print(f"\nModos de Vibração (Autovetores): ")
print(vetores_p.real)