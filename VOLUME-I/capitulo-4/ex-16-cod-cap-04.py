"""

4.4.3 Sinais amortecidos.  - pág.77

"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 500)

A = np.exp(-0.2*t)
x = A * np.sin(4*t)

plt.figure(facecolor='white')  # borda branca da figura
plt.plot(t, x, color='black', linewidth=2)  # curva preta

plt.title('Sinal Amortecido')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.show()