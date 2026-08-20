# -*- coding: utf-8 -*-
"""

7.7.5 Método de Cohen--Coon. pág.446

"""
import numpy as np
import matplotlib.pyplot as plt
import control as ct

# 1. Processo FOPDT: G(s) = 1.5/(10s+1) * exp(-2s)
K, tau, L = 1.5, 10.0, 2.0
Gp = ct.TransferFunction([K], [tau, 1])
num_pade, den_pade = ct.pade(L, 2)  # Padé de 2ª ordem
delay = ct.TransferFunction(num_pade, den_pade)
sys_g = ct.series(Gp, delay)

# Função auxiliar para PID (forma padrão)
def pid_tf(Kc, tauI, tauD):
	s = ct.TransferFunction.s
	return Kc * (1 + 1/(tauI*s) + tauD*s)

# 2. Controladores PID
# Ziegler–Nichols
Kc_zn = 4.0
tauI_zn = 4.0
tauD_zn = 1.0
c_zn = pid_tf(Kc_zn, tauI_zn, tauD_zn)

# Cohen–Coon
Kc_cc = 4.53
tauI_cc = 4.55
tauD_cc = 0.70
c_cc = pid_tf(Kc_cc, tauI_cc, tauD_cc)

# 3. Malhas fechadas
sys_zn = ct.feedback(c_zn * sys_g, 1)
sys_cc = ct.feedback(c_cc * sys_g, 1)

# 4. Resposta ao degrau
t = np.linspace(0, 60, 1000)
t, y_zn = ct.step_response(sys_zn, t)
t, y_cc = ct.step_response(sys_cc, t)

# 5. Gráfico comparativo
plt.figure(figsize=(10, 5))
plt.plot(t, y_zn, 'k--', label='Ziegler–Nichols (Agressivo)')
plt.plot(t, y_cc, 'k-', linewidth=2, label='Cohen–Coon (Equilibrado)')
plt.axhline(y=1.0, color='gray', linestyle=':', label='Setpoint')
plt.title('Comparação de Sintonia: Z–N vs. Cohen–Coon')
plt.xlabel('Tempo (s)')
plt.ylabel('Saída (Temperatura)')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()
