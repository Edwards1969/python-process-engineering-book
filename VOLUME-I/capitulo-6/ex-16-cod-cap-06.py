# -*- coding: utf-8 -*-
"""
6.6.1 Parte 1: Modelagem Analítica com SymPy. - pág.173

"""
import sympy as sp

h, z, R, H = sp.symbols('h z R H')


# Área da seção circular em função da altura z.
area = sp.pi * (H/R * z)**2

# Integral para encontrar a fórmula do volume.
volume_formula = sp.integrate(area, (z, 0, h))

print(f"Fórmula do Volume: {volume_formula}")

# Resultado da saída: Fórmula do Volume: pi*H**2*h**3/(3*R**2)