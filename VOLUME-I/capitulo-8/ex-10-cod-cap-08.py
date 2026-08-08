# -*- coding: utf-8 -*-
"""
8.2.5 Estudo de Caso: Procesamento de Sinal de Pressão Ruidoso.  -  pág.247

"""
import numpy as np
import matplotlib.pyplot as plt

# 1. Simulacao do Sinal Real
fs = 500  # Frequencia de amostragem
t = np.arange(0, 2, 1/fs)
pressao_real = 50 + 2 * np.sin(2 * np.pi * 0.5 * t)  # Osclacao lenta

# 2. Adicao de Ruido (60Hz + Branco)
ruido_rede = 1.5 * np.sin(2 * np.pi * 60 * t)
ruido_branco = np.random.normal(0, 0.8, len(t))
sinal_bruto = pressao_real + ruido_rede + ruido_branco

# 3. Filtro Exponencial (EWMA)
def filtro_exponencial(sinal, alpha):
	y =np.zeros(len(sinal))
	y[0] = sinal[0]
	for k in range(1, len(sinal)):
		y[k] = alpha * sinal[k] + (1 - alpha) * y[k-1]
		return y

sinal_filtrado = filtro_exponencial(sinal_bruto, alpha=0.1)

# 4. FFT para identificar o ruido
fft_bruto = np.abs(np.fft.fft(sinal_bruto))
freqs = np.fft.fftfreq(len(t), 1/fs)

# Visualizacao
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.plot(t, sinal_bruto, label="Sinal Bruto", alpha=0.5)
ax1.plot(t, sinal_filtrado, label="Sinal Filtrado (EWMA)", color='red', lw=2)
ax1.set_title("Sinal de Pressão no Domínio do Tempo")
ax1.legend()

ax2.plot(freqs[:len(t)//2], fft_bruto[:len(t)//2])
ax2.set_title("Espectro de Frequência (Ruído de 60 Hz)")
ax2.set_xlim(0, 100)
ax2.set_xlabel("Frequência (Hz)")

plt.tight_layout()
plt.show()	

