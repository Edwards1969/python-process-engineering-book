# -*- coding: utf-8 -*-
"""

5.11.3 Estudo de casos 3: Monitoramento de Pressão em um Sistema 
Hidráulico. - pág. 129

"""
import pandas as pd
import matplotlib.pyplot as plt

# 1. Importação e conversão de datas
df = pd.read_csv("hidraulico.csv")
df["data"] = pd.to_datetime(df["data"])
df = df.set_index("data")

"""
Explicação:
df = pd.read_csv("hidraulico.csv")  
Lê o arquivo CSV e cria o DataFrame com as colunas data, pressao_bar e vazao_Lmim.

df["data"] = pd.to_datetime(df["data"])  
Converte a coluna data (que era texto) para o formato de data e hora do pandas.

df = df.set_index("data")  
Define a coluna data como índice do DataFrame, transformando a tabela em uma série temporal.
"""

# 2. Filtragem de pressão fora da faixa.
fora_faixa = df[(df["pressao_bar"] < 2 ) | (df["pressao_bar"] > 6)]

"""
Explicação:

Pegue todas as linhas onde a pressão é menor que 2 bar 
 
OU (|)

Pegue todas as linhas onde a pressão é maior que 6 bar

"""

# 3. Reamostragem por hora.
df_horario = df.resample("min").mean()

# 4. Visualização.
plt.plot(df_horario.index, df_horario["pressao_bar"])
plt.xlabel("Tempo (min)")
plt.ylabel("Pressão (bar)")
plt.xticks(rotation=45)
plt.title("Pressão Média Horária do Sistema Hidráulico")
plt.grid(True)
plt.show()






















