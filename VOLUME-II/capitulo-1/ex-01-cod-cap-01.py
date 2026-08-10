# -*- coding: utf-8 -*-
"""

Cap 1- Controle de Processos Aplicado.
1.1.1 Exemplo Prático: Cálculo de Erro em um Sistema de Nível. -pág. 2

"""
import numpy as np

sp = 5.0

leitura_pv = np.array([4.2, 4.5, 4.8, 5.0,5.2, 5.1, 4.9])

print(f"{'Instante':<10} | {'PV (m)':<10} | {'Erro (m)':<10}")
print("-" * 35)

for i, pv in enumerate(leitura_pv):
    erro = sp - pv
print(f"{i:<10} | {pv:<10.2f} | {erro:<10.2f}")

