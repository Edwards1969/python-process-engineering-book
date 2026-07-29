"""
4.3.1 Cores, estilos e espessuras de linha.  - pág. 67

"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 200)
y = np.sin(x)

plt.plot(x, y, color="black", linestyle="--", linewidth=2,)
plt.title("Seno com Estilo Personalizado")
plt.show()