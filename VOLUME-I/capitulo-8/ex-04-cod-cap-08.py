# -*- coding: utf-8 -*-
"""

Exercício 3: Simule em Python um sinalde 30 Hzamostradoa 40 Hz. - pág. 231

"""
import numpy as np
import matplotlib.pyplot as plt

f = 30
fs = 40
t= np.linspace(0, 0.2, 2000)
s = np.sin(2*np.pi*f*t)

td = np.arange(0, 0.2, 1/fs)
sd = np.sin(2*np.pi*f*td)

plt.figure(figsize=(10,4))
plt.plot(t, s, label="Sinal Analógico (30 Hz)", alpha=0.5)

plt.stem(td, sd, linefmt='r', markerfmt='ro', basefmt='k', label="Amostras (40 Hz)")

plt.title("Aliasing: 30 Hz Amostrado a 40 Hz \u2192 Frequência Aparente de 10 Hz")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
















               

