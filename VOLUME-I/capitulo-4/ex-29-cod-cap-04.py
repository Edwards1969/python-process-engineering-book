"""

4.6.4 Curva tensão-deformação.  -  pág. 92-93

"""
import numpy as np
import matplotlib.pyplot as plt

eps = np.array([0.00, 0.01, 0.02, 0.03, 0.04])
sigma = np.array([0, 120, 240, 310, 330])

plt.figure(figsize=(8,5), facecolor="white")

plt.plot(eps, sigma, 
    color='black', 
    linewidth=2, 
    marker='o', 
    markersize=7, 
    markerfacecolor='white',
    markeredgecolor='black'
    )

plt.title('Curva Tensão-Deformação')
plt.xlabel('Deformação')
plt.ylabel('Tensão (MPa)')
plt.grid(True)

# Deixa o gráfico mais "respirável"
plt.xlim(-0.002, 0.042)
plt.ylim(-10, 350)

plt.show()

