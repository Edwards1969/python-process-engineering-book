"""
4.3.3 Anotações no gráfico. - pág. 70

"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200)
y = np.sin(x)

plt.plot(x, y, color="black", linestyle="--", linewidth=2)
plt.title("Seno com Estilo Personalizado")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")

plt.annotate("Máximo", xy=(np.pi/2, 1), xytext=(2, 1.2),
arrowprops=dict(arrowstyle="->"))
plt.xlim(0, 8)
plt.ylim(-0.5, 1.4)
plt.show()
