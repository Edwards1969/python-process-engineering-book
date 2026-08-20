# -*- coding: utf-8 -*-
"""

Efeito do Tempo Morto.pág. 412
Exemplo Computacional 4: Efeito do Tempo Morto

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def pade(L):
	num = [1, -L/2, L**2/12]
	den = [1,  L/2, L**2/12]
	return num, den
num = [1]
den = [10, 1]
sys_no_delay = signal.TransferFunction(num, den)
num_p, den_p = pade(5)
sys_delay = signal.TransferFunction(np.polymul(num, num_p), 
np.polymul(den, den_p))
w = np.logspace(-2, 2, 500)

for sys, label in [(sys_no_delay, "Sem atraso"),
				(sys_delay, "Com atraso (Padé)")]:
	w, mag, phase = signal.bode(sys, w)
	plt.figure(figsize=(10,5))
	plt.subplot(2,1,1)
	plt.semilogx(w, mag, color="black")
	plt.title(label)
	plt.ylabel("Magnitude (dB)")
	plt.grid(True, linestyle=":")
	
	plt.subplot(2,1,2)
	plt.semilogx(w, phase, color="black")
	plt.ylabel("Fase (graus)")
	plt.xlabel("Frequência (rad/s)")
	plt.grid(True, linestyle=":")
	plt.tight_layout()
	plt.show()
