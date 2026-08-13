# -*- coding: utf-8 -*-
"""

3.9 Projeto de Engenharia: Sistema de Monitoramento e 
Inventário de Fluidos. pág. 157

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Carregamento dos dados
df = pd.read_csv("produtos_industriais.csv")

# 2. Constantes de projeto
g = 9.81               # gravidade (m/s²)
H_total = 12.0         # altura total do tanque (m)
P_projeto_kPa = 130.0  # pressão máxima permitida (kPa)

# 3. Cálculos de engenharia
df['Peso_Esp_N_m3'] = df['Densidade_kg_m3'] * g

# Pressão hidrostática com tanque cheio
df['P_Base_Cheio_kPa'] = (df['Peso_Esp_N_m3'] * H_total) / 1000

# 4. Nível máximo seguro
df['Nivel_Seguro_m'] = np.where(
	df['P_Base_Cheio_kPa'] > P_projeto_kPa,
	(P_projeto_kPa * 1000) / df['Peso_Esp_N_m3'],
	H_total
	)

# 5. Identificação de criticidade
df['Critico'] = df['P_Base_Cheio_kPa'] > P_projeto_kPa
print("\n--- Relatório de Inventário e Segurança ---\n")
print(df[['Substancia', 'P_Base_Cheio_kPa', 'Nivel_Seguro_m', 'Critico']])

#---------------------------------------------------------
# Gráfico do perfil de pressão hidrostática
#---------------------------------------------------------
# Simulação de níveis
niveis = np.linspace(0, 12, 100)
plt.figure(figsize=(10, 6))
marcadores = ['o', 's']  # Acetona e Ácido Sulfúrico
for i, subst in enumerate(['Acetona', 'Ácido Sulfúrico']):
	dados = df[df['Substancia'] == subst]
	peso_esp = dados['Peso_Esp_N_m3'].values[0]
	pressao = (peso_esp * niveis) / 1000
	plt.plot(
		niveis,
		pressao,
		color='black',
		marker=marcadores[i],
		markevery=10,
		markerfacecolor='white',
		markeredgecolor='black',
		linewidth=1.6,
		label=subst
	)
    
# Linha de limite estrutural
plt.axhline(
	y=P_projeto_kPa,
	color='black',
	linestyle='--',
	label='Limite Estrutural (130 kPa)'
)
plt.title('Perfil de Pressão Hidrostática: Fluidos Extremos')
plt.xlabel('Nível do Tanque (m)')
plt.ylabel('Pressão na Base (kPa)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

