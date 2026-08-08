# -*- coding: utf-8 -*-
"""

Exercício Extra: Rmoção Específica do Ruído de 60 Hz. - pág. 242

"""
import numpy as np
import matplotlib.pyplot as plt

# 1. Geração do sinal com ruído (25 Hz + ruído de 60 Hz)
fs = 1000  # Frequência de amostragem (1 kHz)
t = np.arange(0, 1.0, 1/fs)

vibracao_motor = np.sin(2 * np.pi * 25 * t)  # Componente de 25 Hz
ruido_60hz = 0.8 * np.sin(2 * np.pi * 60 * t)  # Ruído da rede (60 Hz)
sinal_sujo = vibracao_motor + ruido_60hz + np.random.normal(0, 0.5, len(t))

# 2. FFT do sinal
fft_sinal = np.fft.fft(sinal_sujo)
freqs = np.fft.fftfreq(len(t), 1/fs)

# 3. Cópia do espectro original
fft_notch = fft_sinal.copy()

# 4. Remove apenas a banda de 59 a 61 Hz (notch)
mascara = (np.abs(freqs) > 59) & (np.abs(freqs) < 61)
fft_notch[mascara] = 0

# 5. Reconstrução do sinal filtrado via IFFT
sinal_notch = np.fft.ifft(fft_notch).real

# 6. Plotagem
plt.figure(figsize=(10,4))
plt.plot(t, sinal_sujo, label="Sinal Original", alpha=0.4)
plt.plot(t, sinal_notch, label="Sinal com Notch 60 Hz", color='red')
plt.legend(loc="lower left")
plt.title("Remoção Específica do Ruído de 60 Hz via FFT/IFFT")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()


