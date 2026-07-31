"""

5.7.1 Agrupando dados por uma ou múltiplas categorias.  pág116

"""
import pandas as pd

dados = {
"sensor": ["A", "A", "B", "B", "C", "C"],
"temperatura_C": [22.5, 23.1, 24.0, 23.7, 25.3, 25.1]
}

df = pd.DataFrame(dados)

print(df)

# Para calcular a temperatura média de cada sensor.
temperatura_media = df.groupby("sensor")["temperatura_C"].mean()

print(temperatura_media)

