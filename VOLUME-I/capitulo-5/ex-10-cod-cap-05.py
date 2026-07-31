"""

5.0.1 integração com NumPy: cálculos vetorizados e operações matemáticas. - pág. 123

"""
import numpy as np
import pandas as pd

df = pd.DataFrame({
	"velocidade_m_s": [2.0, 3.5, 4.1, 5.0, 6.2]
})

df["energia_cinetica"] =  0.5 * 2.0 * np.square(df["velocidade_m_s"])

print(df)