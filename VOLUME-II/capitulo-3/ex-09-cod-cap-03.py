# -*- coding: utf-8 -*-
"""

Tanques Pressurizados: Uso de Transmissores Diferenciais. pág. 144

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Parâmetros físicos do fluido e do tanque
# ---------------------------------------------------------
rho = 900        # densidade do óleo (kg/m³)
g = 9.81         # aceleração da gravidade (m/s²)
h_max = 10       # altura máxima do tanque (m)

# ---------------------------------------------------------
# Discretização da coluna de fluido
# ---------------------------------------------------------
h = np.linspace(0, h_max, 200)  # níveis de 0 a 10 m

# ---------------------------------------------------------
# CASO 1: Tanque aberto - pressão hidrostática simples
# ---------------------------------------------------------
P_hidro = rho * g * h  # Pa

tabela_nivel = pd.DataFrame({
	"nivel_m": h,
	"pressao_Pa": P_hidro,
	"pressao_kPa": P_hidro / 1000
})

print("Tabela de calibração - Tanque aberto (hidrostático):")
print(tabela_nivel.head())

# ---------------------------------------------------------
# CASO 2: Tanque pressurizado - transmissor diferencial
# ---------------------------------------------------------
P_topo = 2e5  # 2 bar no topo (Pa)

# Pressão no fundo do tanque (inclui gás + coluna de líquido)
P_fundo = P_topo + rho * g * h

# Pressão diferencial medida pelo transmissor
DP = P_fundo - P_topo  # cancela P_topo → sobra só rho*g*h

tabela_dp = pd.DataFrame({
	"nivel_m": h,
	"DP_Pa": DP,
	"DP_kPa": DP / 1000
})
print("\nTabela de calibração - Tanque pressurizado (transmissor diferencial):")
print(tabela_dp.head())

# ---------------------------------------------------------
# Gráficos lado a lado
# ---------------------------------------------------------
plt.figure(figsize=(12,5))
# Gráfico 1 – Tanque aberto
plt.subplot(1,2,1)
plt.plot(h, P_hidro/1000, color="black", linewidth=1.8)
plt.xlabel("Nível (m)")
plt.ylabel("Pressão (kPa)")
plt.title("Tanque Aberto – Pressão Hidrostática")
plt.grid(True)
# Gráfico 2 – Tanque pressurizado (transmissor diferencial)
plt.subplot(1,2,2)
plt.plot(h, DP/1000, color="black", linewidth=1.8)
plt.xlabel("Nível (m)")
plt.ylabel("Pressão Diferencial (kPa)")
plt.title("Tanque Pressurizado – Transmissor Diferencial")
plt.grid(True)
plt.tight_layout()
plt.show()

