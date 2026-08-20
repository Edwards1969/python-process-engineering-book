# -*- coding: utf-8 -*-
"""

Exemplo Computacional 5: Efeito de Controladores no Bode. pág. 414

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
Gp = signal.TransferFunction([1], [5,1])
Kp = 2
Gc_P  = signal.TransferFunction([Kp], [1])
Gc_PI = signal.TransferFunction([1, 0.5], [1, 0])
Gc_PID = signal.TransferFunction([1, 1, 0.2], [1])
controllers = [
	(Gc_P,  "Controlador P",  "-"),   # linha contínua
	(Gc_PI, "Controlador PI", "--"),  # linha tracejada
	(Gc_PID,"Controlador PID", ":")   # linha pontilhada
]
w = np.logspace(-2, 2, 500)
plt.figure(figsize=(10,5))
for Gc, label, style in controllers:
	# Série manual (SciPy não tem signal.series)
	num = np.polymul(Gc.num, Gp.num)
	den = np.polymul(Gc.den, Gp.den)
	sys = signal.TransferFunction(num, den)
	w, mag, phase = signal.bode(sys, w)
	plt.subplot(2,1,1)
	plt.semilogx(w, mag, linestyle=style, color="black", label=label)
	plt.ylabel("Magnitude (dB)")
	plt.grid(True, linestyle=":")
	plt.subplot(2,1,2)
	plt.semilogx(w, phase, linestyle=style, color="black", label=label)
	plt.ylabel("Fase (graus)")
	plt.xlabel("Frequência (rad/s)")
	plt.grid(True, linestyle=":")
plt.subplot(2,1,1)
plt.legend()
plt.subplot(2,1,2)
plt.legend()
plt.tight_layout()
plt.show()
