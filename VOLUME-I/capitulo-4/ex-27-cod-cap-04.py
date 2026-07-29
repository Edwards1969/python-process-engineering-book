"""

4.6.2 Corrente em um circuito RL.   -  pág. 90

"""
import numpy as np
import matplotlib.pyplot as plt

R = 50
L = 0.2
IO = 2

# Intervalo ajustado para visualizar melhor a curva exponencial
t = np.linspace(0, 0.02, 300)
tau = L / R

i = IO *  (1 - np.exp(-t/tau))

plt.figure(facecolor="white")
plt.plot(t, i, color="black", linewidth=2)
plt.title("Corrente em um Circuito RL")
plt.xlabel("Tempo (s)")
plt.ylabel("Corrente (A)")
plt.grid(True)

#--- Formatação elegante do eixo x ---
ax = plt.gca()
ax.ticklabel_format(style="sci", axis="x", scilimits=(-2, -2))
ax.xaxis.get_offset_text().set_fontsize(12)

plt.show()