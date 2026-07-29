"""
4.2.5 Gráficos múltiplos. - pág. 66

"""
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, 200)

y1 = np.exp(-0.1*t)
y2 = np.exp(-0.2*t)

plt.plot(t, y1, color="black", label="k = 0.1")
plt.plot(t, y2, color="black", label="k = 0.2")

plt.legend()
plt.title("Comparação de Decaimentos")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()