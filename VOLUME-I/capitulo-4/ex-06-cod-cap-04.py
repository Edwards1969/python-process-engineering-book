"""
4.2.4 Histograma - pág. 66

"""

import matplotlib.pyplot as plt
import numpy as np

dados = np.random.normal(50, 5, 1000)

plt.hist(dados, bins=20)
plt.title("Distribuição de Medidas")
plt.xlabel("Valor")
plt.ylabel("Frequência")
plt.show()