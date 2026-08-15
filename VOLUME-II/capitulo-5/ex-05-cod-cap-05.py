# -*- coding: utf-8 -*-
"""

Análise Gráfica da Variação Percentual. - pág. 

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# Simulação da radiação térmica
# -------------------------
# Constante de Stefan-Boltzmann
sigma = 5.670374419e-8

# Temperatura de 900°C a 1100°C
T_C = np.linspace(900, 1100, 100)
T_K = T_C + 273.15

# Fluxo radiativo
Fluxo = sigma * T_K**4

# DataFrame
tabela_radiacao = pd.DataFrame({
			"Temperatura_K": T_K,
			"Fluxo_W_m2": Fluxo
		})

# Variação percentual (em permilagem ‰)
tabela_radiacao["Variacao_percentual"] = (
	tabela_radiacao["Fluxo_W_m2"].pct_change() * 1000
)

# -------------------------
# Gráfico 
# -------------------------
plt.figure(figsize=(10,5))
plt.plot(
	tabela_radiacao["Temperatura_K"],
	tabela_radiacao["Variacao_percentual"],
	color="black",
	linestyle="-",
	linewidth=2,
	label="Variação percentual (‰)"
)
plt.xlabel("Temperatura (K)")
plt.ylabel("Variação percentual (‰)")
plt.grid(True, linestyle="--", color="gray", alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()	
