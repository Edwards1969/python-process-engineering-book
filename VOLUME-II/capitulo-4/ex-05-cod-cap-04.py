# -*- coding: utf-8 -*-
"""

4.9 Comparação Entre Diferentes Instrumentos de Vazão Usando  Python. - pág.191-195

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tempo = np.arange(0, 101, 1)
Q_real = 0.03 + 0.005 * np.sin(0.1 * tempo)

# Simulação dos instrumentos
np.random.seed(42)

# Placa de orifício: ruído moderado e atraso pequeno
Q_orificio = Q_real + np.random.normal(0, 0.0015, len(tempo))

# Venturi: alta precisão e baixo ruído
Q_venturi = Q_real + np.random.normal(0, 0.0005, len(tempo))

# Turbina: ruído baixo, mas sensível a variações rápidas
Q_turbina = Q_real + np.random.normal(0, 0.001, len(tempo))

tabela = pd.DataFrame({
	"Tempo_s": tempo,
	"Q_real": Q_real,
	"Q_orificio": Q_orificio,
	"Q_venturi": Q_venturi,
	"Q_turbina": Q_turbina
})

MAE_orificio = (abs(tabela["Q_orificio"] - tabela["Q_real"])).mean()
MAE_venturi = (abs(tabela["Q_venturi"] - tabela["Q_real"])).mean()
MAE_turbina = (abs(tabela["Q_turbina"] - tabela["Q_real"])).mean()
print("Erro médio - Placa de Orifício: {:.6f}".format(MAE_orificio))
print("Erro médio - Venturi: {:.6f}".format(MAE_venturi))
print("Erro médio - Turbina: {:.6f}".format(MAE_turbina))

# Visualização Comparativa.
plt.plot(
        tabela["Tempo_s"], tabela["Q_real"],
        label="Vazão Real",
        linewidth=2,
        linestyle="-",        # linha contínua
        marker="o",           # marcador para destacar
        markersize=4
        )
plt.plot(
        tabela["Tempo_s"], tabela["Q_orificio"],
        label="Placa de Orifício",
        linewidth=1.8,
        linestyle="--",       # linha tracejada
        )
plt.plot(
        tabela["Tempo_s"], tabela["Q_venturi"],
        label="Venturi",
        linewidth=1.8,
        linestyle="-.",       # traço-ponto
        )
plt.plot(
        tabela["Tempo_s"], tabela["Q_turbina"],
        label="Turbina",
        linewidth=1.8,
        linestyle=":",        # linha pontilhada
        )
plt.xlabel("Tempo (s)")
plt.ylabel("Vazão ($m^3/s$)")
plt.title("Comparação Entre Instrumentos de Vazão")
plt.grid(True)
plt.legend()
plt.show()









