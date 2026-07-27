"""
3.2.2 Funções de criação de arrays - pág. 45
"""
import numpy as np

z = np.zeros(5)
u = np.ones(3)
v = np.arange(0, 10, 2)
t = np.linspace(0, 1, 5)

print(z )
print( u)
print( v)
print(t)

"""
3.2.3 Operações vetoriais - pag. 47
"""
a = np.array([1, 2, 3, 4])
b = a * 2
c = a + 10
d = a**2

print(b)
print(c)
print(d)

"""
3.2.3 Operações entre arrays - pag. 47
"""
x = np.array([2, 4, 6])
y = np.array([1, 1, 1])

soma = x + y
produto = x * y

print(soma, produto)

"""
3.2.5 Aplicação em Engenharia: energia cinética
"""

m = 2.0 # kg
v = np.array([0, 2, 4, 6, 8, 10])

Ec = 0.5 * m * v**2

print(Ec)

"""
3.3 Indexação, Fatiamento e Máscaras - pág. 48
"""

a = np.array([10, 20, 30, 40, 50])

print(a[0])  # primeiro elemento
print(a[3])  # quarto elemento
print(a[-1]) # último elemento

"""
3.3.2 Fatiamento (slicing)
"""
a = np.array([10, 20, 30, 40, 50,  60])
b = a[1:4]  # elemento dos índices 1, 2, e 3-> [20, 30, 40]
c = a[:3]   # primeiros três elementos -> [10, 20, 30]
e = a[::2]  # elementos com passo 2 -> [10, 30, 50]

"""
3.3.3 Indexação em arrays multidimensionais - pág.49
"""
M = np.array([
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
    ])

linha = M[1, :]     # segunda linha
coluna = M[:, 2]    # terceira coluna
bloco = M[0:2, 1:3] # submatriz

"""
3.3.4 Máscaras boleanas - pág. 49
"""

v = np.array([5, 12, 7, 20, 3])

mask = v > 10

print(mask)    # array boleno
print(v[mask]) # elementos maiores que 10

"""
3.3.5 Aplicação em Engenharia: filtragem de dados
"""

pressao = np.array([1.2, 2.5, 3.1, 7.8, 5.0, 6.3])

faixa = (pressao >= 2) & (pressao <= 6)
valores_validos = pressao[faixa]

print(valores_validos)