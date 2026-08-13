# -*- coding: utf-8 -*-
"""

3.6 Medição de Nível Hidrostático. - pág. 141

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Parâmetros físicos do fluido e do tanque
# ---------------------------------------------------------
rho = 900        # densidade do óleo (kg/m³)
g = 9.81         # aceleração da gravidade (m/s²)
h_max = 10       # altura máxima do tanque (m)

# ---------------------------------------------------------
# Discretização da coluna de fluido
# ---------------------------------------------------------
# Criamos 200 valores igualmente espaçados entre 0 e h_max.
# Cada valor representa um nível possível no tanque.
h = np.linspace(0, h_max, 200)

# ---------------------------------------------------------
# Cálculo da pressão hidrostática
# ---------------------------------------------------------
# Implementação direta da equação:
#     P = rho * g * h
# Essa é a relação fundamental usada por transmissores hidrostáticos.
P = rho * g * h

# ---------------------------------------------------------
# Construção da tabela de calibração
# ---------------------------------------------------------
tabela_nivel = pd.DataFrame({
	"nivel_m": h,
	"pressao_Pa": P,
	"pressao_kPa": P / 1000
})

# Exibe as primeiras linhas da tabela
print(tabela_nivel.head())

# ---------------------------------------------------------
# Gráfico da pressão em função do nível
# ---------------------------------------------------------
plt.figure(figsize=(8,5))
plt.plot(h, P/1000, color="black", linewidth=1.8)
plt.xlabel("Nível (m)")
plt.ylabel("Pressão Hidrostática (kPa)")
plt.title("Pressão Hidrostática em Função do Nível")
plt.grid(True)
plt.show()

