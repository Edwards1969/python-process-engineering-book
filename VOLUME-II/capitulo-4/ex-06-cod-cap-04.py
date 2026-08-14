# -*- coding: utf-8 -*-
"""

4.10 Estudo de Caso Industrial: Linha de Água em Processo Contínuo. - pág. 195

"""
import pandas as pd
# Criando os dados ordenados corretamente
tempo = list(range(600))
# DeltaP variando suavemente (mesmo padrão que você usou)
DeltaP = [
        	1200 + i*1.5 for i in range(10)
        ] + [
        	1342 - (i-10)*7 for i in range(10, 100)
        ] + [
        	745 + (i-100)*5.75 for i in range(100, 600)
        ]
# Ajuste final para garantir coerência
DeltaP = DeltaP[:600]

# Temperatura variando de 25 a 28 °C
Temperatura = []
for t in tempo:
	if t < 3:
		Temperatura.append(25)
	elif t < 6:
		Temperatura.append(26)
	elif t < 9:
		Temperatura.append(27)
	else:
		Temperatura.append(28)	
        
# Criando o DataFrame
tabela = pd.DataFrame({
	"Tempo_s": tempo,
	"DeltaP_Pa": DeltaP,
	"Temperatura_C": Temperatura
})

# Salvando o CSV
tabela.to_csv("linha_agua.csv", index=False)
print("Arquivo linha_agua.csv gerado com sucesso!")	

