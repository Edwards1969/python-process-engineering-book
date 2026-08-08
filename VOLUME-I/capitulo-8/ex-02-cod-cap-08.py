"""

Exercícios Resolvidos - Teorema de Nyquist-Shannon. - pág. 232

"""
import numpy as np
import matplotlib.pyplot as plt

f = 45
fs = 90   # Nyquist -> Frequência de Amostragem.
t = np.linspace(0, 0.1, 2000)
s = np.sin(2*np.pi*f*t)

td = np.arange(0, 0.1, 1/fs)
sd = np.sin(2 * np.pi * f * td)

plt.figure(figsize=(10, 4))
plt.plot(t, s, label="Sinal Analógico")
plt.stem(td, sd, linefmt='r-', markerfmt='ro', basefmt='k-', label="Amostras (90 Hz)")
plt.title("Amostragem no Limite de Nyquist (45 Hz \u2192 90 Hz)")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
