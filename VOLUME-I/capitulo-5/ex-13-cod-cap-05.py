# -*- coding: utf-8 -*-
"""

5.11.2 - Estudo de casos 2: Ensio Mecânico de Tração  -  pág. 128

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Importação de dados.
df = pd.read_csv("tracao.csv")

# 2. Propriedade geométrica das amostras.
area = 12.5  # mm
comprimento_inicial = 50  #  mm

# 3. Cálculo de tensão e deformação.
df["tensao_MPa"] = df["forca_N"] / area
df["deformacao"] = df["alongamento_mm"] / comprimento_inicial

# 4. Visualização.
plt.plot(df["deformacao"], df["tensao_MPa"])
plt.xlabel("Deformação (mm)")
plt.ylabel("Tensão (MPa)")
plt.title("Curva Tensão-Deformação")
plt.grid(True)

plt.show()





