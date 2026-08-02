"""

5.9.1 integração com NumPy: cálculos vetorizados e operações matemáticas. - pág. 123

"""
import numpy as np
import pandas as pd

df = pd.DataFrame({
	"velocidade_m_s": [2.0, 3.5, 4.1, 5.0, 6.2]
})

df["energia_cinetica"] =  0.5 * 2.0 * np.square(df["velocidade_m_s"])

print(df)

""""

9.8.2 Integração com Matplotlib: visualização direta a partir do DataFrame. -  pág. 123-124

"""
import matplotlib.pyplot as plt

df["velocidade_m_s"].plot()
plt.xlabel("Índice")
plt.ylabel('Velocidade (m/s)')
plt.title("Variação da Velocidade")
plt.show()