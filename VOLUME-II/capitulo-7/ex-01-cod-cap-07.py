# -*- coding: utf-8 -*-
"""

7.3.1 Representação por Equações Diferenciais. - pág.378

"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# ============================================================
# Modelo de primeira ordem: dy/dt = (K*u(t) - y) / tau
# ============================================================
def modelo_primeira_ordem(y, t, K, tau):
	u = 1.0 if t >= 5 else 0.0   # Degrau aplicado em t = 5 s
	dydt = (K * u - y) / tau
	return dydt

# ============================================================
# Parâmetros do sistema
# ============================================================
K = 2.0
tau = 10.0
y0 = 0.0
t = np.linspace(0, 60, 600)

# ============================================================
# Solução numérica da EDO
# ============================================================
y = odeint(modelo_primeira_ordem, y0, t, args=(K, tau))

# ============================================================
# Gráfico
# ============================================================
plt.figure(figsize=(9, 4.5))
plt.plot(t, y, color='black', linewidth=1.8, label='Resposta do Sistema')
plt.axvline(x=5, color='black', linestyle='--', linewidth=1, label='Degrau em t = 5 s')
plt.xlabel('Tempo (s)')
plt.ylabel('Saída y(t)')
plt.title('Resposta ao Degrau de um Sistema de Primeira Ordem')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
