"""
4.3.1 Limites dos eixos.  - pág. 69

"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 200)
y = np.sin(x)

plt.plot(x, y, color="black", linestyle="--" , linewidth=2)
plt.title("Seno com Estilo Personalizado")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.xlim(0, 8)
plt.ylim(-0.5, 1.2)
plt.show()