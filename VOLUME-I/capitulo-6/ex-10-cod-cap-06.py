"""

Exemplo 1: Integração Numérica com quad. -  pág.157-158

"""
from scipy.integrate import quad
import numpy as np

f = lambda x: np.exp(-x**2)
resultado, erro = quad(f, 0, 1)

print("Integral = ", resultado)
print("Estimativa do erro ", erro)






