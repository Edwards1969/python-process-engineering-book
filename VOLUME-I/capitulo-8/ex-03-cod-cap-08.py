# -*- coding: utf-8 -*-
"""

Exercício 1: Um sinal de 10 Hz é amostrado a 12 Hz - pág. 229-231

"""
import numpy as np
import matplotlib.pyplot as plt

f = 10     # Sinal de 10 Hz
fs = 12    # Sinal de 12 Hz -> frequência de amostragem.
t = np.linspace(0, 1,2000)
s = np.sin(2 * np.pi * f * t)

td = np.arange(0, 1, 1/fs)
sd = np.sin(2 * np.pi * f * td)

plt.figure(figsize=(10,4))
plt.plot(t, s, label="Sinal Analógico (10 Hz)", alpha=0.5)
plt.stem(td, sd, linefmt='r', markerfmt='ro', basefmt='k-', label="Amostras (12 Hz)")

plt.title("Aliasing: 10 Hz Amostrado a 12 Hz \u2192 Frequência Aparente de 2 Hz")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend( )
plt.tight_layout()
plt.show()

