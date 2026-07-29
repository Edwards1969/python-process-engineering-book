"""
4.2.3 Gráfico de barras. -  pág. 65

"""
import matplotlib.pyplot as plt

materiais = ["aço", "Alumínio", "Cobre"]
densidade = [7850, 2700, 8960]

plt.bar(materiais, densidade)
plt.title("Densidade de Materiais")
plt.ylabel("$kg/m^3$")

plt.show()