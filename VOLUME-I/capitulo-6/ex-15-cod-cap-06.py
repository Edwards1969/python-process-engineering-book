# -*- coding: utf-8 -*-
"""

6.5.7 Integração de Dados Discretos (Instrumentação).  -  pág.171-172

"""
from scipy.integrate import simpson
import numpy as np

# Dados coletados de um sensor (exemplo: vazão em m3/h)
tempo = np.array([0, 1, 2, 3, 4, 5])       # horas
vazao = np.array([10, 12, 11, 15, 14, 13]) # m3/h

# Integrando os pontos para obter o volume total acumulado.
volume_total = simpson(y=vazao, x=tempo)

print(f"Volume total acumulado: {volume_total} m3")

