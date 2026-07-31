"""
5.3.1 Leitura de arquivos CSV - págs. 104-105
"""

import pandas as pd

df = pd.read_csv("dados_experimento.csv")
print(df)

"""
Observação

Se o programa gerar o erro:

FileNotFoundError: [Errno 2] No such file or directory

verifique se o arquivo "dados_experimento.csv" está localizado na mesma
pasta do programa Python.

Se o arquivo estiver na pasta correta e o erro persistir, configure o
Visual Studio Code para executar o script utilizando a pasta do próprio
arquivo como diretório de trabalho:

1. Pressione Ctrl + Shift + P.
2. Digite: Preferences: Open Workspace Settings (JSON)
3. Pressione Enter.
4. O Visual Studio Code abrirá (ou criará) o arquivo:

   .vscode/settings.json

5. Adicione:

{
    "python.terminal.executeInFileDir": true
}

Essa configuração precisa ser realizada apenas uma vez.
"""
