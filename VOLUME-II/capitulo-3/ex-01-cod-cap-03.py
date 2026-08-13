# -*- coding: utf-8 -*-
"""

3.2.1 Simulação Computacional da Pressão Hidrostática. pág. 123

"""
import numpy as np
import pandas as pd

# Parâmetros do fluido e do tanque
rho = 950        # densidade (kg/m³) - óleo típico
g = 9.81         # gravidade (m/s²)
h_max = 12       # altura máxima do tanque (m)

# Discretização da coluna de fluido
h = np.linspace(0, h_max, 200)

# Pressão hidrostática
P = rho * g * h

# Tabela para análise
tabela_pressao = pd.DataFrame({
	"altura_m": h,
	"pressao_Pa": P,
	"pressao_kPa": P/1000
})
tabela_pressao.head()

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
plt.plot(h, P/1000, color="black", linewidth=1.8)
plt.xlabel("Altura da Coluna (m)")
plt.ylabel("Pressão (kPa)")
plt.grid(True)
plt.title("Pressão Hidrostática em Função da Altura")
plt.show()
