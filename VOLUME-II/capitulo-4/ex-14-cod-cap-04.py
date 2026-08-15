# -*- coding: utf-8 -*-
"""

4.17 Técnicas Modernas de Instrumentação Baseadas em 
Machine Learning. pág.227-223

"""
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd

# ---------------------------------------------------------
# 1. Carregando os dados originais
# ---------------------------------------------------------
tabela = pd.read_csv("dados_ml_vazao.csv")

# ---------------------------------------------------------
# 2. Transformações necessárias
#    (mantém consistência de unidades para o modelo)
# ---------------------------------------------------------
tabela["DeltaP_Pa"] = tabela["DP_kPa"] * 1000          # kPa → Pa
tabela["Vazao_m3_s"] = tabela["Vazao_m3_h"] / 3600     # m³/h → m³/s

# ---------------------------------------------------------
# 3. Seleção das variáveis de entrada e saída
# ---------------------------------------------------------
X = tabela[["DeltaP_Pa", "Temperatura_C", "Densidade_kg_m3"]]
y = tabela["Vazao_m3_s"]

# ---------------------------------------------------------
# 4. Divisão dos dados em treino e teste
# ---------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42
)

# ---------------------------------------------------------
# 5. Modelo de Machine Learning
# ---------------------------------------------------------
modelo = RandomForestRegressor(n_estimators=200)
modelo.fit(X_train, y_train)

# ---------------------------------------------------------
# 6. Previsões
# ---------------------------------------------------------
y_pred = modelo.predict(X_test)

print(y_pred)

from sklearn.metrics import mean_absolute_error
	
erro = mean_absolute_error(y_test, y_pred)
print("Erro médio absoluto:", erro)
