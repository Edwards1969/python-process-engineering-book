# -*- coding: utf-8 -*-
"""

7.4.4 Efeito de Zeros e Tempo Morto. - pág.400

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# ============================================================
# Parâmetros do processo
# ============================================================
K = 1.0
tau = 20.0
L = 15.0  # tempo morto

# Sistema sem tempo morto: G0(s) = K / (tau s + 1)
num = [K]
den = [tau, 1]
sys_no_delay = signal.TransferFunction(num, den)

# Aproximação de Padé (2ª ordem) para o tempo morto
def pade_approx(L):
	num = [1, -L/2, L**2/12]
	den = [1,  L/2, L**2/12]
	return num, den
num_pade, den_pade = pade_approx(L)

# Sistema com tempo morto aproximado: G(s) = G0(s) * e^{-Ls}
num_delay = np.polymul(num, num_pade)
den_delay = np.polymul(den, den_pade)
sys_delay = signal.TransferFunction(num_delay, den_delay)

# ============================================================
# Resposta ao degrau
# ============================================================
t = np.linspace(0, 120, 1000)
t1, y_no_delay = signal.step(sys_no_delay, T=t)
t2, y_delay = signal.step(sys_delay, T=t)

# ============================================================
# Gráfico comparativo
# ============================================================
plt.figure(figsize=(10,5))
plt.plot(t1, y_no_delay, label="Sem tempo morto")
plt.plot(t2, y_delay, "--", label="Com tempo morto (Padé)")
plt.title("Efeito do Tempo Morto na Resposta ao Degrau")
plt.xlabel("Tempo (s)")
plt.ylabel("Saída")
plt.grid(True, linestyle=":")
plt.legend()
plt.tight_layout()
plt.show()

"""

7.5 Análise de Sistemas no Domínio da Frequência. - pág.405

7.5.1 Diagramas de Bode - pág.

"""

import matplotlib.pyplot as plt
from scipy import signal
num = [1]
den = [10, 1]
sys = signal.TransferFunction(num,den)
w, mag, phase = signal.bode(sys)
plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.semilogx(w, mag, color="black")
plt.ylabel("Magnitude (dB)")
plt.grid(True, linestyle=":")
plt.subplot(2,1,2)
plt.semilogx(w, phase, color="black")
plt.ylabel("Fase (graus)")
plt.xlabel("Frequência (rad/s)")
plt.grid(True, linestyle=":")
plt.tight_layout()
plt.show()


"""

Contribuições de Polos e Zeros. - pág.408

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
Gp = signal.TransferFunction([1], [1, 1])
Gz = signal.TransferFunction([1, 1], [1])
w = np.logspace(-2, 2, 500)
for sys, label in [(Gp, "Polo em -1"), (Gz, "Zero em -1")]:
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













