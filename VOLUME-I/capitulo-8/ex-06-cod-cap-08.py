# -*- coding: utf-8 -*-
"""

Exercício Resolvido em Python: Comparação de Filtros no Domínio do Tempo. - 

"""
import numpy as np
import matplotlib.pyplot as plt

# Sinal original  (vazão simulada)
t = np.linspace(0, 10, 1000)
sinal = 5 + 0.5*np.sin(2*np.pi*0.5*t)  # dinâmica lenta
ruido = np.random.normal(0, 0.3, len(t))
sinal_r = sinal + ruido

# --- Filtro de Média Móvel ---
N = 10
media_movel = np.convolve(sinal_r, np.ones(N)/N, mode='same')

# --- Filtro Exponencial (EWMA) ---
alpha = 0.1
ewma = np.zeros_like(sinal_r)
ewma[0] = sinal_r[0]
for k in range(1, len(sinal_r)):
    ewma[k] = alpha*sinal_r[k] + (1-alpha)*ewma[k-1]
    
# --- Filtrao Passa-BAixo Discreto ---
dt = t[1] - t[0]
tau  = 0.5
beta = dt / (tau + dt)

lp = np.zeros_like(sinal_r)
lp[0] = sinal_r[0]
for k in range(1, len(sinal_r)):
    lp[k] = lp[k-1] + beta * (sinal_r[k] -  lp[k-1])
    
# --- Plotagem ---
plt.figure(figsize=(12, 6))
plt.plot(t, sinal_r, label='Sinal Ruidoso', alpha=0.4)

plt.plot(t, media_movel, label='Média Móvel (N=10)')
plt.plot(t, ewma, label='EWMA ($\\alpha=0.1$)')
plt.plot(t, lp, label='Passa-Baixa Discreto ($\\tau=0.5$)')
plt.plot(t, sinal, label='Sinal Real', linewidth=2, color='black')
plt.legend()
plt.grid(True)
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Comparação de Filtros no Domínio do Tempo')
plt.show()











    
    



























