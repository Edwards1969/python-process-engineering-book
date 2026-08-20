# -*- coding: utf-8 -*-
"""

Exemplo Prático: Efeito da Filtragem Derivativa. pág.463

"""
import numpy as np
import matplotlib.pyplot as plt

# Tempo e sinal de erro com ruído moderado
t = np.linspace(0, 10, 5000)
dt = t[1] - t[0]
e = np.sin(t) + 0.02*np.random.randn(len(t))  # ruído reduzido

# Parâmetros do controlador derivativo
Kc, tauD = 2.0, 0.5

tau_f = 0.1  # filtro mais forte

# Derivada ideal
de_dt = np.gradient(e, t)
d_ideal = Kc * tauD * de_dt

# Derivada filtrada (filtro de 1ª ordem)
d_filt = np.zeros_like(e)
for k in range(1, len(t)):
	d_filt[k] = d_filt[k-1] + (dt/tau_f)*(d_ideal[k] - d_filt[k-1])
    
# Gráfico
plt.figure(figsize=(9,5))
plt.plot(t, d_ideal, 'k--', label='Derivada Ideal (ruidosa)')
plt.plot(t, d_filt, 'k-', linewidth=2, label='Derivada Filtrada')
plt.legend()
plt.grid(True, linestyle=':')
plt.title('Comparação da Ação Derivativa: Ideal vs Filtrada')
plt.tight_layout()
plt.show()
