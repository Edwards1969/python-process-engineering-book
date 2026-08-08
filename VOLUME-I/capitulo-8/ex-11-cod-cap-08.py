# -*- coding: utf-8 -*-
"""
Exercício Extra: Remoção Específica do Ruído de 60 Hz.  -  pág. 249

"""
import numpy as np
import matplotlib.pyplot as plt

# 1. Geração do sinal com ruído (25 Hz + ruído de 60 Hz)
fs = 500  # Frequência de amostragem
t = np.arange(0, 2, 1/fs)

pressao_real = 50 + 2 * np.sin(2 * np.pi * 0.5 * t)  # Oscilação lenta (0.5 Hz)
ruido_rede = 1.5 * np.sin(2 * np.pi * 60 * t)        # Ruído de 60 Hz
ruido_branco = np.random.normal(0, 0.8, len(t))      # Ruído térmico
sinal_bruto = pressao_real + ruido_rede + ruido_branco

# 2. FFT do sinal bruto
fft_sinal = np.fft.fft(sinal_bruto)
freqs = np.fft.fftfreq(len(t), 1/fs)

# 3. Cópia do espectro
fft_notch = fft_sinal.copy()

# 4. Remove apenas a banda de 59 a 61 Hz
mascara = (np.abs(freqs) > 59) & (np.abs(freqs) < 61)
fft_notch[mascara] = 0

# 5. Reconstrução via IFFT
sinal_notch = np.fft.ifft(fft_notch).real

# 6. Plotagem
plt.figure(figsize=(10,4))
plt.plot(t, sinal_bruto, label="Sinal Bruto", alpha=0.4)
plt.plot(t, sinal_notch, label="Sinal com Notch 60Hz", color='green')
plt.legend()
plt.title("Remoção Específica do Ruído de 60 Hz")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()	
