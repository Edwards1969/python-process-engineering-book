# -*- coding: utf-8 -*-
"""

Análise Gráfica do Termistor NTC, pág. 283

"""
import numpy as np
import matplotlib.pyplot as plt

# Faixa de temperatura (°C)
T_C = np.linspace(0, 100, 500)
T_K = T_C + 273.15

# Parâmetros do NTC
R0 = 10000      # resistência nominal em T0
T0 = 298.15     # temperatura de referência (25 °C)
B  = 3950       # constante B

# Modelo exponencial do NTC
R = R0 * np.exp(B * (1/T_K - 1/T0))

# Gráfico R(T)
plt.figure(figsize=(7,4))
plt.plot(T_C, R, label="R(T)")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Resistência (Ohms)")
plt.title("Curva de Resistência do Termistor NTC")
plt.grid(True)
plt.tight_layout()
plt.show()

