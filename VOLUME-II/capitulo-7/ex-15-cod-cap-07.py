# -*- coding: utf-8 -*-
"""

7.7.7 Sintonia IMC (Internal Model Control). - pág. 452
Exemplo Prático: Sintonia FOPDT Geral de um Processo de Vazão. pág. 454

"""
import numpy as np
import matplotlib.pyplot as plt
import control as ct

# Processo FOPDT
K, tau, L = 2.0, 8.0, 1.5
Gp = ct.TransferFunction([K], [tau, 1])
num_pade, den_pade = ct.pade(L, 2)  # Padé de 2ª ordem
delay = ct.TransferFunction(num_pade, den_pade)
sys = ct.series(Gp, delay)

# Controlador PI (forma padrão)
def pi_tf(Kc, tauI):
	s = ct.TransferFunction.s
	return Kc * (1 + 1/(tauI * s))

# Parâmetros PI calculados
Kc = 1.04
tauI = 8.72
controller = pi_tf(Kc, tauI)

# Malha fechada
closed = ct.feedback(controller * sys, 1)

# Resposta ao degrau
t = np.linspace(0, 60, 1000)
t, y = ct.step_response(closed, t)
plt.figure(figsize=(9,5))
plt.plot(t, y, 'k-', linewidth=2)
plt.axhline(1, color='gray', linestyle=':')
plt.title('Sintonia FOPDT Geral – Controlador PI')
plt.xlabel('Tempo (s)')
plt.ylabel('Saída')
plt.grid(True, linestyle=':')
plt.tight_layout()
plt.show()
