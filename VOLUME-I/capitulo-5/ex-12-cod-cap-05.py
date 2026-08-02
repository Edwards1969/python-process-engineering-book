"""

5.11.1 Estudo de Casos 1: Análise de Temperatura em um Processo Térmico. - pág. 126

"""
import pandas as pd
import matplotlib.pyplot as plt

# 1.Importação dos dados.
df = pd.read_csv("temperatura-processo.csv")

# 2. Cálculo de média móvel (janela de 10 segundos)
df["media_movel"] = df["temperatura_C"].rolling(window=10).mean()

#3. Visualização.
plt.plot(df["tempo_s"], df["temperatura_C"], label="Temperatura")
plt.plot(df["tempo_s"], df["media_movel"], label="Média Móvel", linewidth=2)
plt.xlabel("Tempo (s)")
plt.ylabel("Temperatura ($^oC$)")
plt.title("Evolução Térmica do Processo")
plt.legend()
plt.grid(True)

plt.show()                           






