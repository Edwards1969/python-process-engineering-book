""""
Exemplo: Classificação de Esforço Mecânico.
"""

forca = 350 # N

if forca < 200:
    print("Esforço baixo.")
elif forca < 400:
    print("Esforço moderado.")
else:
    print("Esforço elevado. Avaliar integridade do componente.")
