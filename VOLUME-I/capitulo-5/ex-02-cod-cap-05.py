"""

5.2.2 A estrutura DataFrame: tabela completa para análises multidimensionais.  -  pág. 103

"""

import pandas as pd

dados ={
    "tempo_s": [0, 1, 2, 3, 4],
    "temperatua_C": [22.5,  23.1, 24.0, 24.8, 25.3],
    "pressao_kPa": [101.2, 102.5, 100.8, 99.7, 101.9]
}

df = pd.DataFrame(dados)
print(df)

""""

5.3.1 A estrutura Series: vetores rotulados para dados uidimensionais.   -  pág. 104

"""
import pandas as pd

pressao = pd.Series([101.2, 102,5, 100.8, 99.7, 101.9])
print(pressao)