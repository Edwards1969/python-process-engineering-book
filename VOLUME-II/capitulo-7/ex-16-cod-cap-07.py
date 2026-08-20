# -*- coding: utf-8 -*-
"""

Exemplo Prático: Sintonia FOPDT Geral de um Processo de Vazão. pág.454

"""
import numpy as np
import matplotlib.pyplot as plt
import control as ct

# Processo térmico FOPDT
K, tau, L = 1.2, 12.0, 3.0
Gp = ct.TransferFunction([K], [tau, 1])
num_pade, den_pade = ct.pade(L, 2)  # Padé de 2ª ordem
delay = ct.TransferFunction(num_pade, den_pade)
sys = ct.series(Gp, delay)

# Controlador PI (forma IMC)
def pi_tf(Kc, tauI):
	s = ct.TransferFunction.s
	return Kc * (1 + 1/(tauI * s))

# Sintonia IMC (PI)
Kc = 1.67
tauI = 15.0
controller = pi_tf(Kc, tauI)

# Malha fechada
closed = ct.feedback(controller * sys, 1)

# Resposta ao degrau
t = np.linspace(0, 120, 1000)
t, y = ct.step_response(closed, t)
plt.figure(figsize=(9,5))
plt.plot(t, y, 'k-', linewidth=2)
plt.axhline(1, color='gray', linestyle=':')
plt.title('Sintonia IMC – Controlador PI')
plt.xlabel('Tempo (s)')
plt.ylabel('Temperatura')
plt.grid(True, linestyle=':')
plt.tight_layout()
plt.show()
