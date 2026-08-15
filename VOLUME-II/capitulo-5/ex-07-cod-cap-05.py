# -*- coding: utf-8 -*-
"""

5.4.4 Sensores de Resistência (Pt100). pág. 275-277

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Faixa de temperatura (°C)
T = np.linspace(0, 200, 500)

# Constantes do sensor Pt100
R0 = 100
a = 3.908e-3
b = -5.775e-7

# Resistência
R = R0*(1 + a*T + b*T**2)

# Sensibilidade analítica
sensibilidade = R0*(a + 2*b*T)

# Criação da tabela de dados: 	
tabela_pt100 = pd.DataFrame({
		"Temperatura_C": T,
		"Resistencia_ohm": R,
		"dR_dT": sensibilidade
	})


# --- Gráfico 1: Resistência ---
plt.figure(figsize=(7,4))
plt.plot(T, R, label="R(T)")
plt.xlabel("Temperatura (C)")
plt.ylabel("Resistência (Ohms)")
plt.title("Curva de Resistência do Pt100")
plt.grid(True)
plt.tight_layout()
plt.savefig("pt100_resistencia.png", dpi=300)

# --- Gráfico 2: Sensibilidade ---
plt.figure(figsize=(7,4))
plt.plot(T, sensibilidade, color="red", label="dR/dT") 
plt.xlabel("Temperatura (C)")
plt.ylabel("Sensibilidade (Ohms/C)")
plt.title("Sensibilidade do Pt100 em Função da Temperatura")
plt.grid(True)
plt.tight_layout()
plt.savefig("pt100_sensibilidade.png", dpi=300)	

# Exercício Avançado — Erro de Linearização - pág.279

# Ajuste linear
coef = np.polyfit(T, R, 1)
R_lin = np.polyval(coef, T)
erro = R - R_lin
erro_max = np.max(np.abs(erro))

# Inversão Numérica: Resistência → Temperatura. pág. 280
# Resistência medida simulada
R_med = 138.5  # ohms

# Estimativa inicial
T_est = 100.0

for _ in range(10):  
	# "_" indica variável descartável
	f  = R0*(1 + a*T_est + b*T_est**2) - R_med
	df = R0*(a + 2*b*T_est)
	T_est = T_est - f/df
    
print("A Temperatura estimada é = {:.2f} °C".format(T_est))
