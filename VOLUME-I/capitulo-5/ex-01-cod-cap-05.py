"""

5.1 Introdução ao Pandas.  - pág. 101

"""
import pandas as pd

dados = {
    "tempo_s": [0, 1, 2, 3, 4],
    "temperatura_C": [22.5, 23.1, 24.0, 24.8, 25.3]
}

df = pd.DataFrame(dados)
print(df)

"""

5.2.1 A estrutura Series: vetores rotulados para dados unidimensionais

"""
import pandas as pd

pressao = pd.Series([101.2, 102.5, 100.8, 99.7, 101.9])
print(pressao)
