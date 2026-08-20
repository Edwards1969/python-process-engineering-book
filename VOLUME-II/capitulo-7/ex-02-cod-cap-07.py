# -*- coding: utf-8 -*-
"""

Representação em Espaço de Estado. - pág. 382

"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# ============================================================
# Modelo de segunda ordem em espaço de estados
# x[0] = y(t)      (saída)
# x[1] = dy/dt     (velocidade)
# ============================================================
def modelo_segunda_ordem(x, t, K, zeta, wn):
	y, v = x
	u = 1.0 if t >= 5 else 0.0   # Degrau aplicado em t = 5 s
	
	dy_dt = v
	dv_dt = K * wn**2 * u - 2 * zeta * wn * v - wn**2 * y
	
	return [dy_dt, dv_dt]

# ============================================================
# Parâmetros do sistema
# ============================================================
K = 2.0
zeta = 0.2      # Subamortecido
wn = 1.0
x0 = [0.0, 0.0] # Condições iniciais
t = np.linspace(0, 60, 600)

# ============================================================
# Solução numérica da EDO
# ============================================================
sol = odeint(modelo_segunda_ordem, x0, t, args=(K, zeta, wn))

# ============================================================
# Gráfico
# ============================================================
plt.figure(figsize=(9, 4.5))
plt.plot(t, sol[:, 0], color='black', linewidth=1.8, label='Resposta do Sistema (2ª ordem)')
plt.axvline(x=5, color='black', linestyle='--', linewidth=1, label='Degrau em t = 5 s')
plt.xlabel('Tempo (s)')
plt.ylabel('Saída y(t)')
plt.title('Resposta ao Degrau de um Sistema de Segunda Ordem')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()

