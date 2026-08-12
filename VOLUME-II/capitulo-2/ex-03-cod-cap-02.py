# -*- coding: utf-8 -*-
"""

2.2.7 Aplicação Prática: Seleção de Válvulas para Segurança e Controle. pág.86

"""
import numpy as np
import matplotlib.pyplot as plt

# Sinal de controle de 0 a 100% (normalizado de 0 a 1)
u = np.linspace(0, 1, 100)

# 1. Caracteristica Linear
q_linear = u

# 2. Caracteristica Abertura Rapida (Quick Opening)
q_quick = np.sqrt(u)

# 3. Caracteristica Igual Percentual (Normalizada para partir do zero)
R = 30 # Rangeabilidade
q_eq_raw = (R**u) / R
q_eq_perc = (q_eq_raw - q_eq_raw[0]) / (q_eq_raw[-1] - q_eq_raw[0])

# --- Plotagem Tecnica ---
plt.figure(figsize=(10, 6))
plt.plot(u*100, q_linear*100, label='Linear', color='black', linestyle='--')
plt.plot(u*100, q_quick*100, label='Abertura Rapida (Seguranca)', color='black', linewidth=2)
plt.plot(u*100, q_eq_perc*100, label='Igual Percentual (Controle)', color='black', linestyle=':')

# Destaque do ponto critico de 20%
plt.scatter([20], [np.sqrt(0.2)*100], color='black', label='Ponto de Seguranca (20%)')
plt.title('Dinamica de Valvulas: Vazao vs. Sinal de Controle')
plt.xlabel('Sinal de Controle u (%)')
plt.ylabel('Vazao de Fluido q (%)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

