# -*- coding: utf-8 -*-
"""

3.3 Transmissores Industriais. pág.125

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Faixa do transmissor
Pmin = 0      # bar
Pmax = 20     # bar

# Pressões simuladas
P = np.linspace(Pmin, Pmax, 200)

# Conversão para corrente (mA)
I = 4 + 16 * (P - Pmin) / (Pmax - Pmin)

tabela_tx = pd.DataFrame({
	"pressao_bar": P,
	"corrente_mA": I
})
tabela_tx.head()

plt.figure(figsize=(8,5))
plt.plot(I, P, color="black", linewidth=1.8)
plt.xlabel("Corrente (mA)")
plt.ylabel("Pressão (bar)")
plt.title("Curva de Calibração de um Transmissor 4–20 mA")
plt.grid(True)
plt.show()
