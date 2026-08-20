# -*- coding: utf-8 -*-
"""

7.6.3 Controle Feedforward. pág.431

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#---------------------------------
# 1. Processo e Perturbação
# Gp = 1/(10s+1), Gd = 0.8/(10s+1)
#---------------------------------
sys_gp = signal.TransferFunction([1], [10, 1])
sys_gd = signal.TransferFunction([0.8], [10, 1])

# 2. Controladores
Kp_fb = 2.0      # Ganho do Feedback
G_ff = -0.8      # Ganho Feedforward ideal

# 3. Simulação temporal
t = np.linspace(0, 80, 1000)
disturb = np.where(t >= 10, 1.0, 0.0)  # Perturbação em t = 10 s

# 4. Resposta apenas com Feedback:
num_fb_only = [0.8]
den_fb_only = [10, 1 + Kp_fb]  # 10s + 3
sys_fb_only = signal.TransferFunction(num_fb_only, den_fb_only)
_, y_fb, _ = signal.lsim(sys_fb_only, disturb, t)

# 5. Resposta combinada (Feedback + Feedforward):
num_comb = [0.8 + (G_ff * 1)]  # 0.8 - 0.8 = 0 → cancelamento perfeito
den_comb = [10, 1 + Kp_fb]
sys_comb = signal.TransferFunction(num_comb, den_comb)
_, y_comb, _ = signal.lsim(sys_comb, disturb, t)

# 6. Gráfico comparativo
plt.figure(figsize=(8, 5))
plt.plot(t, y_fb, color='black', linestyle='--', label='Apenas Feedback')
plt.plot(t, y_comb, color='black', linewidth=2, label='Feedback + Feedforward')
plt.title('Rejeição de Perturbação: Efeito do Controle Feedforward')
plt.xlabel('Tempo (s)')
plt.ylabel('Desvio do Nível (m)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()

# 7. Impressão dos valores máximos
print(f"Máximo desvio apenas FB: {np.max(np.abs(y_fb)):.4f}")
print(f"Máximo desvio FB + FF: {np.max(np.abs(y_comb)):.4f}")

