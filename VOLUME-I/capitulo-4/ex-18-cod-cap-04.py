"""

4.4.5 Resposta de sistemas dinâmicos.  - pág.79

"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 300)
tau = 2

y = 1 - np.exp(-t/tau)

plt.figure(facecolor='white') # borda branca da figura
plt.plot(t, y, color='black', linewidth=2)  # curva preta

plt.title('Reposta ao Degrau de $1^a$ ordem')
plt.xlabel('Tempo (s)')
plt.ylabel('Saída')
plt.grid(True)
plt.show()