# -*- coding: utf-8 -*-
"""

7.7 Controladores PID. - pág. 435
7.7.1 Ação Proporcional, Integral e Derivativa - pág. 437

"""
import numpy as np
import matplotlib.pyplot as plt
import control as ct

# 1. Processo de segunda ordem: G(s) = 1 / (s^2 + 2s + 1)
num_p = [1]
den_p = [1, 2, 1]
Gp = ct.TransferFunction(num_p, den_p)

# 2. Parâmetros do controlador
Kc = 10.0
tauI = 2.0
tauD = 1.0

# 3. Função auxiliar para gerar controladores P, PI, PD e PID
def pid_tf(Kc, tauI=None, tauD=None):
	s = ct.TransferFunction.s
	# P
	if tauI is None and tauD is None:
		return Kc
	# PI
	if tauI is not None and tauD is None:
		return Kc * (1 + 1/(tauI * s))
	# PD
	if tauI is None and tauD is not None:
		return Kc * (1 + tauD * s)
	# PID
	return Kc * (1 + 1/(tauI * s) + tauD * s)

# 4. Malhas fechadas
sys_p   = ct.feedback(pid_tf(Kc) * Gp, 1)
sys_pi  = ct.feedback(pid_tf(Kc, tauI=tauI) * Gp, 1)
sys_pd  = ct.feedback(pid_tf(Kc, tauD=tauD) * Gp, 1)
sys_pid = ct.feedback(pid_tf(Kc, tauI=tauI, tauD=tauD) * Gp, 1)

# 5. Respostas ao degrau
t = np.linspace(0, 15, 1000)
t, y_p   = ct.step_response(sys_p, t)
t, y_pi  = ct.step_response(sys_pi, t)
t, y_pd  = ct.step_response(sys_pd, t)
t, y_pid = ct.step_response(sys_pid, t)

# 6. Gráfico comparativo (PADRONIZADO)
plt.figure(figsize=(10, 6))
plt.plot(t, y_p,   'k--', label='P')
plt.plot(t, y_pi,  'k:',  label='PI')
plt.plot(t, y_pd,  'k-.', label='PD')
plt.plot(t, y_pid, 'k-', linewidth=2, label='PID')

# Setpoint padronizado (igual ao exemplo ZN vs CC)
plt.axhline(y=1.0, color='gray', linestyle=':', label='Setpoint')
plt.title('Efeito das Ações P, PI, PD e PID na Resposta do Sistema')
plt.xlabel('Tempo (s)')
plt.ylabel('Saída do Processo')
plt.legend(loc='lower right')
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()

