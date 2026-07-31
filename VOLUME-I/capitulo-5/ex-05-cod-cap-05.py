""""

5.3.3 Leitura de arquivos de texto.  -  pág 106-107

"""
import pandas as pd

df = pd.read_csv("temperaturas.txt", sep="\t")  # arquivo separado por tabulações
print(df)         # mostra os dados.
print(df.columns) # mostra os nomes das colunas.
print(df.dtypes)  # mostra os tipos dos dados em cada coluna.

""""
Observação:

Ao ler arquivos de texto separados por tabulação (sep="\t"), certifique‑se de que o arquivo realmente contém TAB entre as colunas.
Alguns editores, como o Visual Studio Code, podem substituir TAB por espaços, fazendo com que o Pandas interprete o arquivo como uma única coluna.

Se isso acontecer, ajuste o VS Code:

1.Abra File → Preferences → Settings.

2.Pesquise por insert spaces.

3.Desmarque: Editor: Insert Spaces.

4.Desmarque: Editor: Detect Indentation.

5.Mantenha marcado: Editor: Use Tab Stops.

Depois disso, ao pressionar TAB no arquivo .txt, o VS Code passará a inserir tabulação real, permitindo que o Pandas leia corretamente arquivos separados por TAB.
"""