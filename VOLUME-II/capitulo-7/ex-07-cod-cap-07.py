# -*- coding: utf-8 -*-
"""

Margem de Ganho e Margem de Fase. - pág. 410

"""
import numpy as np
import matplotlib.pyplot as plt
import control as ct

# Sistema G(s) = 5 / [(2s+1)(5s+1)]
num = [5]
den = np.polymul([2, 1], [5, 1])
sys = ct.TransferFunction(num, den)

# Bode (sem plot automático)
mag, phase, w = ct.bode(sys, dB=True, plot=False)

# --- Gráfico igual ao do SciPy ---
plt.figure(figsize=(10,6))

# Magnitude
plt.subplot(2,1,1)
plt.semilogx(w, 20*np.log10(mag), color="black")
plt.ylabel("Magnitude (dB)")
plt.grid(True, linestyle=":")

# Fase
plt.subplot(2,1,2)
plt.semilogx(w, phase * 180/np.pi, color="black")
plt.ylabel("Fase (graus)")
plt.xlabel("Frequência (rad/s)")
plt.grid(True, linestyle=":")
plt.tight_layout()
plt.show()

# --- Margens de estabilidade ---
gm, pm, wg, wp = ct.margin(sys)

# gm vem como ganho absoluto → converter para dB
gm_db = 20*np.log10(gm) if gm != np.inf else np.inf

print("Margem de ganho (dB):", gm_db)
print("Margem de fase (graus):", pm)
print("Frequência de ganho cruzado (rad/s):", wg)
print("Frequência de fase cruzada (rad/s):", wp)



