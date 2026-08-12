# -*- coding: utf-8 -*-
"""

2.2.8 Extensão da Dinâmica de Atuadores: Características Hiperbólicas e de 
Rangeabilidade. pág.88

"""
import numpy as np
import matplotlib.pyplot as plt

# Configuracao do eixo de abertura (0 a 100%)
x = np.linspace(0.0, 1.0, 100)

# Parametros de Rangeabilidade
R1 = 20
R2 = 50

# --- Definicao e Normalizacao para que todas iniciem em Zero ---
# 1. Abertura Rapida (Raiz Quadrada)
f_quick = np.sqrt(x)

# 2. Linear
f_linear = x

# 3. Igual Percentual R=20 (Normalizada)
f_eq20_raw = R1**(x-1)
f_eq20 = (f_eq20_raw - f_eq20_raw[0]) / (f_eq20_raw[-1] - f_eq20_raw[0])

# 4. Igual Percentual R=50 (Normalizada)
f_eq50_raw = R2**(x-1)
f_eq50 = (f_eq50_raw - f_eq50_raw[0]) / (f_eq50_raw[-1] - f_eq50_raw[0])

# 5. Hiperbolica R=20 (Normalizada)
f_hip20_raw = 1 / (R1 - (R1 - 1) * x)
f_hip20 = (f_hip20_raw - f_hip20_raw[0]) / (f_hip20_raw[-1] - f_hip20_raw[0])

# 6. Hiperbolica R=50 (Normalizada)
f_hip50_raw = 1 / (R2 - (R2 - 1) * x)
f_hip50 = (f_hip50_raw - f_hip50_raw[0]) / (f_hip50_raw[-1] - f_hip50_raw[0])

# --- Plotagem Tecnica (Monocromatica) ---
plt.figure(figsize=(10, 7))
plt.plot(x, f_quick, label='Abertura Rapida', color='black', linestyle='--')
plt.plot(x, f_linear, label='Linear', color='black', linewidth=2)
plt.plot(x, f_eq20, label='Igual Percentual (R=20)', color='black', marker='s', markevery=10)
plt.plot(x, f_eq50, label='Igual Percentual (R=50)', color='black', marker='>', markevery=10)
plt.plot(x, f_hip20, label='Hiperbolico (R=20)', color='black', linestyle=':')
plt.plot(x, f_hip50, label='Hiperbolico (R=50)', color='black', marker='*', markevery=10)
plt.xlabel('Fracao de Abertura (x)')
plt.ylabel('Vazao Normalizada $f(x_v)$')
plt.title('Comparativo de Caracteristicas Inerentes (Normalizadas para Origem)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.show()

