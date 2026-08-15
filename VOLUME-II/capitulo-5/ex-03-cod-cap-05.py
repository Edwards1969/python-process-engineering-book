# -*- coding: utf-8 -*-
"""

Modelo do Processo Térmico. - pág. 263

"""
import numpy as np
import matplotlib.pyplot as plt
# Tempo
dt = 1
tempo = np.arange(0, 800, dt)
# Processo real
T_real = 80 + 20*np.sin(0.02*tempo)
# --- Termopar ---
tau_tc = 5
T_tc = np.zeros_like(T_real)
ruido_tc = np.random.normal(0, 0.5, len(T_real))

for i in range(1, len(T_real)):
	T_tc[i] = T_tc[i-1] + (T_real[i] - T_tc[i-1]) / tau_tc

T_tc_med = T_tc + ruido_tc
# --- Pt100 ---
tau_pt = 12
T_pt = np.zeros_like(T_real)
ruido_pt = np.random.normal(0, 0.2, len(T_real))

for i in range(1, len(T_real)):
	T_pt[i] = T_pt[i-1] + (T_real[i] - T_pt[i-1]) / tau_pt

T_pt_med = T_pt + ruido_pt
# Erro Médio Absoluto
ema_tc = np.mean(np.abs(T_real - T_tc_med))
ema_pt = np.mean(np.abs(T_real - T_pt_med))

print("EMA Termopar:", round(ema_tc,3))
print("EMA Pt100:", round(ema_pt,3))

# Gráfico comparativo em preto e branco
plt.figure(figsize=(10,5))

plt.plot(tempo, T_real,
		linestyle='-',
		color='black',
		linewidth=2,
		label="Sensor Ideal")

plt.plot(tempo, T_tc_med,
		linestyle='--',
		color='black',
		label="Termopar")

plt.plot(tempo, T_pt_med,
		linestyle=':',
		color='black',
		label="Pt100")

plt.xlabel("Tempo (s)")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)
plt.show()
