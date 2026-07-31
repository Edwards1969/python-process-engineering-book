# Python Aplicado à Engenharia de Processos Industriais  
### Códigos, Exemplos e Exercícios — Volume I e Volume II  
### *Python Applied to Industrial Process Engineering — Code, Examples, and Exercises*

---

## 📘 Sobre o Projeto / About This Project

Este repositório contém todos os códigos, exemplos, exercícios e materiais complementares dos livros:

- **Python Aplicado à Engenharia de Processos Industriais — Volume I**  
- **Python Aplicado à Engenharia de Processos Industriais — Volume II**

Os livros apresentam uma abordagem prática e científica para o uso de Python na engenharia de processos, incluindo fundamentos de programação, computação científica, modelagem, simulação e análise de dados.

---

This repository contains all code, examples, exercises, and supplementary materials from the books:

- **Python Applied to Industrial Process Engineering — Volume I**  
- **Python Applied to Industrial Process Engineering — Volume II**

The books provide a practical and scientific approach to using Python in process engineering, including programming fundamentals, scientific computing, modeling, simulation, and data analysis.

---

## 📂 Estrutura do Repositório / Repository Structure

```
python-process-engineering-book/


│
├── VOLUME-I/
│   ├── capitulo-1/
│   ├── capitulo-2/
│   ├── ...
│   └── capitulo-10/
│
├── VOLUME-II/
│   ├── capitulo-1/
│   ├── capitulo-2/
│   ├── ...
│   └── capitulo-7/
│
└── README.md

```

Cada capítulo contém:

- README.md bilíngue  
- códigos Python  
- exemplos práticos  
- exercícios resolvidos e propostos  

---

Each chapter contains:

- bilingual README.md  
- Python scripts  
- practical examples  
- solved and proposed exercises  

---

## 🧪 Tecnologias Utilizadas / Technologies Used

- **Python 3.x**  
- NumPy  
- SciPy  
- Matplotlib  
- Pandas  
- Jupyter Notebook  

---

## ⚙️ Configuração do Ambiente / Environment Setup

Para que os exemplos sejam executados exatamente como apresentados nos livros, recomenda-se configurar o Visual Studio Code para utilizar a pasta do próprio arquivo Python como diretório de trabalho.

### Visual Studio Code

1. Pressione:

```
Ctrl + Shift + P
```

2. Digite:

```
Preferences: Open Workspace Settings (JSON)
```

3. Pressione **Enter**.

4. O Visual Studio Code abrirá (ou criará) o arquivo:

```
.vscode/settings.json
```

5. Adicione a seguinte configuração:

```json
{
    "python.terminal.executeInFileDir": true
}
```

Com essa configuração, arquivos auxiliares (como arquivos CSV, imagens e outros conjuntos de dados utilizados nos exemplos) serão encontrados automaticamente, sem necessidade de alterar os códigos apresentados nos livros.

> **Observação**
>
> Todos os códigos deste repositório foram mantidos exatamente como publicados nos livros. A configuração acima garante que os exemplos possam ser executados sem necessidade de alterar caminhos para arquivos ou adaptar o código ao ambiente de desenvolvimento.

"""
Observação

Se o programa gerar o erro:

FileNotFoundError: [Errno 2] No such file or directory

verifique se o arquivo "dados_experimento.csv" está localizado na mesma
pasta do programa Python.

Caso utilize o Visual Studio Code, consulte a seção
"Configuração do Ambiente (Environment Setup)" no README.md do repositório,
onde é apresentada a configuração recomendada para executar todos os exemplos
deste livro.
"""

---

## ⚙️ Environment Setup

To run the examples exactly as presented in the books, it is recommended to configure Visual Studio Code so that each Python script is executed using its own folder as the working directory.

### Visual Studio Code

1. Press:

```
Ctrl + Shift + P
```

2. Type:

```
Preferences: Open Workspace Settings (JSON)
```

3. Press **Enter**.

4. Visual Studio Code will open (or create) the following file:

```
.vscode/settings.json
```

5. Add the following setting:

```json
{
    "python.terminal.executeInFileDir": true
}
```

With this configuration, auxiliary files (such as CSV files, images, and other datasets used throughout the examples) will be automatically located without modifying the source code provided in the books.

> **Note**
>
> All source codes in this repository are identical to those published in the books. This configuration ensures that all examples can be executed without modifying file paths or adapting the source code to a specific development environment.

---

## 🎯 Objetivo / Purpose

Fornecer uma base sólida para estudantes, engenheiros e pesquisadores que desejam aplicar Python na engenharia de processos industriais, com foco em:

- automação de cálculos  
- modelagem matemática  
- simulação de processos  
- análise de dados  
- computação científica  

---

Provide a solid foundation for students, engineers, and researchers who want to apply Python to industrial process engineering, focusing on:

- automation of calculations  
- mathematical modeling  
- process simulation  
- data analysis  
- scientific computing  

---

## 📬 Contato / Contact

Para dúvidas, sugestões ou contribuições, utilize a seção **Issues** deste repositório.

Autor: Elilton Edwards

GitHub: https://github.com/Edwards1969

---

For questions, suggestions, or contributions, please use the **Issues** section of this repository.

Author: Elilton Edwards

GitHub: https://github.com/Edwards1969
