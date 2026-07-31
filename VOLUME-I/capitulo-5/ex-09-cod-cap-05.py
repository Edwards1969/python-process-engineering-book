"""

5.7.4 Exemplo aplicado: análise de eficiêcia por máquina.

"""
import pandas as pd

dados = {
	"maquina": ["M1", "M1", "M2", "M2", "M3", "M3"],
	"eficiencia": [0.92, 0.95,0.88,  0.90, 0.97, 0.96]
}
df = pd.DataFrame(dados)
print(df)

eficiencia_maquina = df.groupby("maquina")["eficiencia"].mean()
print(eficiencia_maquina)