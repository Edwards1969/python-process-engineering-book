"""

5.4.1 Seleção de colunas e linhas.  - pág. 109

"""
import pandas as pd

df = pd.read_csv("temperaturas.txt", sep="\t")
print(df)

temperatura = df["temperatura_C"]
print(temperatura)


# Seleção de linhas específicas:
linha_2 = df.loc[2]  # linha com índice 2
linha_0 = df.iloc[0] # primeira linha 

print(linha_2)
print(linha_0)

"""
Observação: 

Os exemplos que estão na página 110 

altas = df[def["temperatura_C]] > 24]

e 

faixa = df[(df["pressao_kPa"] >= 100) & (df["pressao_kPa"] <= 102)]

têm carater ilustrativo e não dependem especificamente do arquivo temperatura.txt
"""