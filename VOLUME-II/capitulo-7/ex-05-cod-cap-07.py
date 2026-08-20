# -*- coding: utf-8 -*-
"""

7.4.3 Sistemas de Ordem Elevada. - pág.395

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# ============================================================
# Parâmetros do sistema de ordem elevada
# ============================================================
K = 1.0
tau1 = 5.0
tau2 = 20.0
tau3 = 80.0

# Sistema de 3ª ordem: G(s) = K / ((tau1 s + 1)(tau2 s + 1)(tau3 s + 1))
num_high = [K]
den_high = np.polymul([tau1, 1], np.polymul([tau2, 1], [tau3, 1]))
sys_high = signal.TransferFunction(num_high, den_high)

# Aproximação de 1ª ordem dominante: G1(s) = K / (tau3 s + 1)
num_1 = [K]
den_1 = [tau3, 1]
sys_1 = signal.TransferFunction(num_1, den_1)

# Aproximação de 2ª ordem dominante: G2(s) = K / ((tau2 s + 1)(tau3 s + 1))
num_2 = [K]
den_2 = np.polymul([tau2, 1], [tau3, 1])
sys_2 = signal.TransferFunction(num_2, den_2)

# ===========================================================
# Resposta ao degrau
# ============================================================
t = np.linspace(0, 600, 1000)  # janela de tempo suficiente para o regime permanente
t_high, y_high = signal.step(sys_high, T=t)
t_1, y_1 = signal.step(sys_1, T=t)
t_2, y_2 = signal.step(sys_2, T=t)

# ============================================================
# Gráfico comparativo
# ============================================================
plt.figure(figsize=(10,5))
plt.plot(t_high, y_high, color="black", linewidth=2, label="Ordem elevada (3ª ordem)")
plt.plot(t_1, y_1, "--", color="gray", label="Aproximação 1ª ordem dominante")
plt.plot(t_2, y_2, ":", color="dimgray", label="Aproximação 2ª ordem dominante")
plt.title("Comparação de Respostas ao Degrau: Sistema de Ordem Elevada e Modelos Reduzidos")
plt.xlabel("Tempo (s)")
plt.ylabel("Saída")
plt.grid(True, linestyle=":")
plt.legend()
plt.tight_layout()
plt.show()
