"""
5.3.2 Leitura de arquivos Excel - 105-106
"""

import pandas as pd

df = pd.read_excel("medicoes_laboratorio.xlsx")
print(df)

"""
Observação

Diferentemente dos arquivos CSV, planilhas do Microsoft Excel (.xlsx)
podem ficar bloqueadas quando abertas no próprio Excel. Nessa situação,
a função pandas.read_excel() poderá gerar o erro:

PermissionError: [Errno 13] Permission denied

Isso ocorre porque o Excel pode impedir que outros programas acessem a
planilha enquanto ela estiver aberta para edição. A solução é simples:
feche a planilha no Excel e execute novamente o programa.
"""