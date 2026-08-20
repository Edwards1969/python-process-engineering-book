# -*- coding: utf-8 -*-
"""

7.6.2 Controle em Cascata. - pág. 726

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# --------------------------------------------
# 1. Dinâmicas de Processo
# G2 (Vazão - rápida): 1 / (s + 1)
# G1 (Temperatura - lenta): 1 / (10s + 1)
# --------------------------------------------

sys_g2 = signal.TransferFunction([1], [1, 1])
sys_g1 = signal.TransferFunction([1], [10, 1])

# 2. Ganhos Proporcionais
Kp_escravo = 10.0  # Malha interna
Kp_mestre = 2.0    # Malha externa

# 3. Malha Interna Fechada (G_int)
num_int = [Kp_escravo]
den_int = [1, 1 + Kp_escravo]
sys_int = signal.TransferFunction(num_int, den_int)

# --------------------------------------------
# 4. Malha Global em Cascata (G_mf)
# G_mf(s) = 20 / (10s^2 + 111s + 31)
# --------------------------------------------

num_mf = [Kp_mestre * Kp_escravo]  # 20
den_mf = [10, 111, 31]
sys_mf = signal.TransferFunction(num_mf, den_mf)

# 5. Resposta ao Degrau
t = np.linspace(0, 80, 1000)
t, y = signal.step(sys_mf, T=t)

# 6. Valor final teórico (DC gain)
y_ss = (Kp_mestre * Kp_escravo) / 31  # 20/31

# 7. Gráfico Técnico
plt.figure(figsize=(8, 5))
plt.plot(t, y, color='black', linewidth=1.5,
		label='Resposta em Cascata (Temperatura)')

plt.axhline(y=1.0, color='black', linestyle=':',
		label='Setpoint Desejado')

plt.axhline(y=y_ss, color='black', linestyle='--', alpha=0.5,
		label=f'Valor Final Teórico: {y_ss:.3f}')
plt.title('Simulação de Controle em Cascata: Temperatura e Vazão')
plt.xlabel('Tempo (s)')
plt.ylabel('Temperatura (°C)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()

# 8. Impressão dos valores
print(f"Valor Final Teórico (20/31): {y_ss:.4f}")
print(f"Valor Final Simulado:       {y[-1]:.4f}")

