"""

4.4.6 Comparação de modelos.  - pág. 80-81

"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 300)

y1 = 1 - np.exp(-t/1)
y2 = 1 - np.exp(-t/2)
y3 = 1 - np.exp(-t/4)

plt.figure(facecolor='white')  # borda branca da figura.

plt.plot(t, y1, color='black', linewidth=2, label='tau = 1')
plt.plot(t, y2, color='black', linewidth=2, linestyle='--' , label='tau = 2')
plt.plot(t, y3, color='black', linewidth=2, linestyle=':' ,label='tau = 4')

plt.title('Comparação de Constantes de Tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Saída')
plt.grid(True)
plt.legend()
plt.show()