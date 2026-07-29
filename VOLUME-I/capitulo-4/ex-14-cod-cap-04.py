"""
4.4.1 Funções matemáticas.  - pág. 76

"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)
y = x**2 - 3*x + 2

plt.figure(facecolor='white')  # borda branca da figura
plt.plot(x, y, color='black', linewidth=2) # curva preta
plt.title("Função Quadrática")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()