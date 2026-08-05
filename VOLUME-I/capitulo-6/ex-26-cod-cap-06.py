"""

6.7.18 Exercício 7: Integração Numérica de DAdos de Potência.  -  pág.191

"""
import numpy as np
from scipy.integrate import trapezoid

# Dados amostrados: Tempos (s) e Potência (W)
tempo = np.array([0, 2, 4, 6, 8, 10])
potencia = np.array([200, 220, 250, 260, 240, 230])

# Cálculo da energia totl consumida em Joules