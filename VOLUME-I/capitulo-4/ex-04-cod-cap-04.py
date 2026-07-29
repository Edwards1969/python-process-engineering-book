"""
4.2.2 Gráfico de dispersão. - pág. 64

"""
import matplotlib.pyplot as plt

x = [20, 25, 30, 35, 40]
y = [90, 95, 100, 110, 120]

plt.figure(facecolor='white') # fundo branco da figura
plt.scatter(x, y, color='black', s=60) # pontos pretos e maiores
plt.title("Relação entre Temperatura e Pressão")
plt.xlabel("Temperatura ($^oC$)")
plt.ylabel("Pressão (kPa)")
plt.grid(True)

plt.show()