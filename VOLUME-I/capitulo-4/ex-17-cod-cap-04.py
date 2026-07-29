"""

4.4.4 Envelope de sinais. - pág. 78-79

"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 500)

portadora = np.sin(20*t)
envelope = np.exp(-0.3*t)

plt.figure(facecolor='white')  # borda branca da figura.

# Sinal modulado (curva preta)
plt.plot(t, portadora*envelope, color='black', linewidth=2, label='Sinal Modulado')

# Envelope superior (vermelho tracejado)
plt.plot(t, envelope,  color='red', linestyle='--', linewidth=2, label='Envelope')

# Envelope inferior (vermelho tracejado)
plt.plot(t, -envelope, color='red', linestyle='--', linewidth=2)

plt.title('Envelope de um Sinal')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()