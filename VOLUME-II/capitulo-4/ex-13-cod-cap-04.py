# -*- coding: utf-8 -*-
"""

4.16 Modelagem de Vazão Multifásica (Óleo–Gás–Água). - pág. 220-226

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# Etapa 1 — Definição do vetor de tempo
# ============================================================
tempo = np.arange(0, 301, 1)   # 0 a 300 s, passo de 1 s

# ============================================================
# Etapa 2 — Modelagem sintética das frações volumétricas
# ============================================================
# Parâmetros do modelo das frações
a_o, b_o, c_o = 0.60, 0.05, 0.02
a_w, b_w, c_w = 0.30, 0.03, 0.015

# Frações variando no tempo
alpha_o = a_o + b_o * np.sin(c_o * tempo)
alpha_w = a_w + b_w * np.cos(c_w * tempo)
alpha_g = 1 - (alpha_o + alpha_w)   # fechamento volumétrico

# ============================================================
# Etapa 3 — Densidades das fases e densidade da mistura
# ============================================================
rho_o = 820     # kg/m³
rho_w = 1000    # kg/m³
rho_g = 50      # kg/m³

# Densidade da mistura
rho_m = alpha_o*rho_o + alpha_w*rho_w + alpha_g*rho_g

# ============================================================
# Etapa 4 — Modelagem sintética das vazões individuais
# ============================================================
A_o, B_o, C_o = 0.02, 0.002, 0.05
A_w, B_w, C_w = 0.01, 0.001, 0.04
A_g, B_g, C_g = 0.005, 0.0005, 0.03

Q_o = A_o + B_o * np.sin(C_o * tempo)
Q_w = A_w + B_w * np.cos(C_w * tempo)
Q_g = A_g + B_g * np.sin(C_g * tempo)

# ============================================================
# Etapa 5 — Vazão total da mistura
# ============================================================
Q_total = Q_o + Q_w + Q_g

# ============================================================
# Etapa 6 — Construção da tabela final
# ============================================================
tabela = pd.DataFrame({
	"Tempo_s": tempo,
	"alpha_o": alpha_o,
	"alpha_w": alpha_w,
	"alpha_g": alpha_g,
	"rho_m": rho_m,
	"Q_total_m3_s": Q_total
})

# Gráfico da Vazão Total.
plt.figure(figsize=(10,5))
plt.plot(tabela["Tempo_s"], tabela["Q_total_m3_s"], color="blue")
plt.xlabel("Tempo (s)")
plt.ylabel("Vazão Total (m³/s)")
plt.title("Variação da Vazão Multifásica (Óleo–Gás–Água)")
plt.grid(True)
plt.show()
















