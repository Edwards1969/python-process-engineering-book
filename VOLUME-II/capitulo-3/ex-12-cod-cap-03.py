# -*- coding: utf-8 -*-
"""

3.8 Projeto de Engenharia: Monitoramento de Tanques Multifluidos. - pág. 153

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#---------------------------------------------------------
# Dataset de substâncias
#---------------------------------------------------------
data = {
	'Substancia': ['Água', 'Etanol', 'Glicerina', 'Diesel', 'Ácido Sulfúrico'],
	'Densidade_kg_m3': [997, 789, 1260, 830, 1840],
	'Massa_Molar_g_mol': [18.01, 46.07, 92.09, 170.0, 98.07]
}
df = pd.DataFrame(data)

#---------------------------------------------------------
# Cálculo do peso específico (gamma = rho * g)
#---------------------------------------------------------
g = 9.81
df['Peso_Especifico_N_m3'] = df['Densidade_kg_m3'] * g

#---------------------------------------------------------
# Pressão máxima para 12 m
#---------------------------------------------------------
altura_tanque = 12.0
df['Pressao_Max_kPa'] = (df['Peso_Especifico_N_m3'] * altura_tanque) / 1000

#---------------------------------------------------------
# Verificação de segurança
#---------------------------------------------------------
pressao_limite = 120.0  # kPa
df['Seguro'] = df['Pressao_Max_kPa'] <= pressao_limite

#---------------------------------------------------------
# Nível máximo permitido
#---------------------------------------------------------
df['Nivel_Max_Seguro_m'] = np.where(
	df['Seguro'],
	altura_tanque,
	(pressao_limite * 1000) / df['Peso_Especifico_N_m3']
)
print(df[['Substancia', 'Pressao_Max_kPa', 'Seguro', 'Nivel_Max_Seguro_m']])

#---------------------------------------------------------
# Gráfico do perfil de pressão hidrostática
#---------------------------------------------------------
niveis = np.linspace(0, 12, 100)
plt.figure(figsize=(10, 6))
marcadores = ['o', 's', '^', 'D', 'x']  # marcadores diferentes
for i, row in df.iterrows():
	pressao_perfil = (row['Peso_Especifico_N_m3'] * niveis) / 1000
	plt.plot(
		niveis,
		pressao_perfil,
		color='black',
		marker=marcadores[i],
		markevery=10,
		markerfacecolor='white',
		markeredgecolor='black',
		linewidth=1.5,
		label=row['Substancia']
	)
plt.axhline(
	y=120,
	color='black',
	linestyle='--',
	label='Limite de Segurança (120 kPa)'
)
plt.title('Perfil de Pressão Hidrostática por Substância')
plt.xlabel('Nível do Tanque (m)')
plt.ylabel('Pressão na Base (kPa)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
