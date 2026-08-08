# -*- coding: utf-8 -*-
"""

8.2.2 Transformada de Fourier e Análise Espectral - pág.240-241

Exemplo prático e Computaciona: Detecção de Falhas em Motores.

"""
import numpy as np
import matplotlib.pyplot as plt

# 1. Geracao do sinal com ruido (Vibracao Real + Ruido 60Hz)
fs = 1000  # Frequencia de amostragem (1 kHz)
t = np.arange(0, 1.0, 1/fs)
vibracao_motor = np.sin(2 * np.pi * 25 * t)  # Sinal de 25 Hz
ruido_60hz = 0.8 * np.sin(2 * np.pi * 60 * t) # Ruido da rede
sinal_sujo = vibracao_motor + ruido_60hz + np.random.normal(0, 0.5, len(t))

# 2. Calculo da FFT (Fast Fourier Transform)
fft_sinal = np.fft.fft(sinal_sujo)
freqs = np.fft.fftfreq(len(t), 1/fs)

# Parte positiva do espectro
n = len(t) // 2
plt.figure(figsize=(10, 5))
plt.plot(freqs[:n], np.abs(fft_sinal[:n]) * 2 / len(t))
plt.title("Análise Espectral (FFT) do Sinal de Vibração")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()














