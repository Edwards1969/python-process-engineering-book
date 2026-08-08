# -*- coding: utf-8 -*-
"""
9.1 Motivação para a Modelagem Dinâmica de Processos Industriais. - pág. 254

"""
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do tanque.
A = 1.0    # Área da seção transversal (m^2)
q_in = 0.8 # vazão de entrada (m^3/s)
h0 = 0.0   # nível inicial (m)

# Simulação simples: h(t) = h0 + (q_in/A) * t
t = np.linspace(0, 50, 200)
h = h0 + (q_in / A) * t

plt.plot(t, h)
plt.xlabel("Tempo (s)")
plt.ylabel("Nível (m)")
plt.title("Evolução do nível em um tanque simples")
plt.grid()
plt.show()
