"""

4.6.5 Sinal amortecido em vibrações.  - pág. 94

"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 500)

A = np.exp(-0.2 * t)
x = A * np.sin(4 * t)

plt.figure(figsize=(8,5), facecolor='white')

plt.plot(t, x, color='black', linewidth=2)
plt.title('Sinal Amortecido')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.show()
