"""

4.6.1 Resposta de um sistema massa-mola.  -  pág.90

"""
import numpy as np
import matplotlib.pyplot as plt

A = 0.05
m = 2.0
k = 200

omega = np.sqrt(k/m)
t = np.linspace(0, 5, 500)

x = A * np.cos(omega * t)

plt.figure(facecolor="white")
plt.plot(t, x, color="black", linewidth=2)
plt.title("Resposta de um Sistema Massa-Mola")
plt.xlabel("Tempo (s)")
plt.ylabel("Deslocamento (m)")
plt.grid(True)

plt.show()

