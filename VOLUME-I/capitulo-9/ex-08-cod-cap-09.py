# -*- coding: utf-8 -*-
"""

9.7 Introdução à Modelagem Multifásica Simplificada. pág. 271-273.

"""
import numpy as np
import matplotlib.pyplot as plt

# Vazões de entrada (kg/s)
mgin = 5.0
moin = 8.0
main = 6.0

# Vazões de saída (kg/s) - valores arbitrários
mgout = 4.0
moout = 7.0
maout = 5.5

# Tempo de simulação
t = np.linspace(0, 50, 500)
dt = t[1] - t[0]

# Massas acumuladas
Mg = np.zeros_like(t)
Mo = np.zeros_like(t)
Ma = np.zeros_like(t)

# Condições iniciais
Mg[0] = 10.0
Mo[0] = 20.0
Ma[0] = 15.0

# Balanços independentes
for k in range(1, len(t)):
	Mg[k] = Mg[k-1] + (mgin - mgout) * dt
	Mo[k] = Mo[k-1] + (moin - moout) * dt
	Ma[k] = Ma[k-1] + (main - maout) * dt

# Gráfico
plt.plot(t, Mg, label="Gás")
plt.plot(t, Mo, label="Óleo")
plt.plot(t, Ma, label="Água")
plt.xlabel("Tempo (s)")
plt.ylabel("Massa acumulada (kg)")
plt.title("Dinâmica simplificada de um sistema trifásico")
plt.grid()
plt.legend()
plt.show()	

