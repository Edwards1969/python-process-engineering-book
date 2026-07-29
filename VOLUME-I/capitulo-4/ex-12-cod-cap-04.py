"""
4.3.4 Grade e legendas avançadas. - pág. 72

"""
import numpy as np
import matplotlib.pyplot as plt

# Geração do vetor de ponto
x = np.linspace(0, 10, 500)

# Funções seno e cosseno
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plotagem das curvas
plt.plot(x, y_sin, color="black", label="Seno", linewidth=2)
plt.plot(x, y_cos, color="black", linestyle="--", label="Cosseno", linewidth=2)

# Personalizações
plt.title("Seno e Cosseno")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True, linestyle=":", linewidth=0.7)
plt.legend(loc="upper right")

# Exibição
plt.show()