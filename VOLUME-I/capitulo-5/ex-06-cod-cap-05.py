"""
5.3.3 Leitura de arquivos de texto. ...cont pág. 107

"""
import pandas as pd

df = pd.read_csv("dados.txt", sep=r"\s+")
print(df)

"""
Observação:
Versões mais recentes do pandas deixaram de aceitar o parâmetro delim_whitespace=True.
Por isso, ao ler arquivos de texto onde as colunas são separadas por espaços, o código:

df = pd.read_csv("dados.txt", delim_whitespace=True)

pode gerar erro.

A forma recomendada atualmente é usar:

pode gerar erro.

df = pd.read_csv("dados.txt", sep=r"\s+")


"""