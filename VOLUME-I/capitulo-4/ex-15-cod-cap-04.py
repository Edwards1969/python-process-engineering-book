"""

4.4.2 Sinais periódicos.  - pág. 76

"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 500)

seno = np.sin(2*t)
cosseno = np.cos(2*t)

plt.figure(facecolor='white') # borda branca da figura
plt.plot(t, seno, color='black', linewidth=2, label='Seno')
plt.plot(t, cosseno, color='black', linestyle='--', linewidth=2, label='Cosseno')

plt.title('Sinais Periódicos')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()