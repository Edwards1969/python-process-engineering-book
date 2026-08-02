"""

5.9.3 Exemplo completo: fluxo de análise em Engenharia.  -  pág. 125

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Importação dos dados
df = pd.read_csv("dados_ensaio_completo.csv")

# 2. Cálculo de grandezas derivadas.
df["energia_cinetica"] = 0.5 * df["massa_kg"] * np.square(df["velocidade_m_s"])

# 3, Filtragem de valores fora da faixa operacional.
df_filtrado = df[df["temperatura_C"] < 80]

# 4. Visualização.
plt.plot(df_filtrado["tempo_s"], df_filtrado["energia_cinetica"] )
plt.xlabel("Tempo (s)")
plt.ylabel("Energia Cinética (J)")
plt.title("Energia Cinética ao Longo do Tempo.")
plt.grid(True)

plt.show()








