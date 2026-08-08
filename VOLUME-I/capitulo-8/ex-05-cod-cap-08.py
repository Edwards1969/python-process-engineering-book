# -*- coding: utf-8 -*-
"""

Simulação de Amostragem com Python. - pág. 232

"""
import numpy as np
import matplotlib.pyplot as plt

# Sinal contínuo (simulado com alta resolução)
f_sinal = 60 # Frequência do sinal em Hz.
t_continuo = np.linspace(0, 0.1, 1000)
sinal_continuo = np.sin(2 * np.pi * f_sinal * t_continuo)

# Amostragem digital.
f_amostragem = 150  # Superior ao dobro de 60 Hz (atende Nyquist)
t_amostrado = np.arange(0, 0.1, 1/f_amostragem)
sinal_amostrado = np.sin(2 * np.pi * f_sinal * t_amostrado)

# Visualização.
plt.figure(figsize=(10, 4))
plt.plot(t_continuo, sinal_continuo, label="Sinal Analógico (Real)", alpha=0.5)
plt.stem(t_amostrado, sinal_amostrado, 
         linefmt='r-', 
         markerfmt='ro', 
         basefmt='k-', 
         label='Sinal Digital (Amostrado')

plt.title("Amostragem de um Sensor de Vibração (60 Hz)")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
















