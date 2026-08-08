# -*- coding: utf-8 -*-
"""
Exercício Proposto: Limpeza de Sinal via IFFT.  -  pág. 244

"""
import numpy as np
import matplotlib.pyplot as plt

# 1. Geração do sinal com ruído (25 Hz + ruído de 60 Hz)
fs = 1000  # Frequência de amostragem (1 kHz)
t = np.arange(0, 1.0, 1/fs)

vibracao_motor = np.sin(2 * np.pi * 25 * t)          # Componente útil (25 Hz)
ruido_60hz = 0.8 * np.sin(2 * np.pi * 60 * t)        # Ruído elétrico (60 Hz)
sinal_sujo = vibracao_motor + ruido_60hz + np.random.normal(0, 0.5, len(t))

# 2. FFT do sinal
fft_sinal = np.fft.fft(sinal_sujo)
freqs = np.fft.fftfreq(len(t), 1/fs)

# 3. Filtro passa‑baixa espectral (< 40 Hz)
fft_filtrada = fft_sinal.copy()
fft_filtrada[np.abs(freqs) > 40] = 0   # Mantém apenas frequências abaixo de 40 Hz

# 4. Reconstrução do sinal filtrado via IFFT
sinal_limpo = np.fft.ifft(fft_filtrada).real

# 5. Plotagem
plt.figure(figsize=(10, 4))
plt.plot(t, sinal_sujo, label="Sinal Ruidoso", alpha=0.4)
plt.plot(t, sinal_limpo, label="Sinal Filtrado (Espectral)", color='red')
plt.legend(loc="lower left")
plt.title("Sinal Recuperado via IFFT (Filtro < 40 Hz)")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()	

