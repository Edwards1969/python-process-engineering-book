"""

4.3.7 Aplicação em Engenharia: curva tensão-deformação

"""
import matplotlib.pyplot as plt
import numpy as np

eps = np.array([0.00, 0.01, 0.02, 0.03, 0.04])
sigma = np.array([0, 120, 240, 310, 330])

plt.figure(facecolor="white")  # fundo branco nas bordas do gráfico

plt.plot(eps, sigma, color="black", marker="o", linewidth=2)
plt.title("Curva Tensão-Deformação")
plt.xlabel("Deformação")
plt.ylabel("Tensão (MPa)")
plt.grid(True)
plt.show()