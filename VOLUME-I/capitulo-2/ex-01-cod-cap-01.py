"""
2.3.1 Exemplo: Verificação de Temperatura - página 33
"""
temperatura = 92

if temperatura < 80: 
    print("Temperatura dentro da faixa segura.")
elif 80 <= temperatura <= 100:
    print("Atenção: temperatura elevada, monitorar o sistema.")
else:
    print("Alerta crítico: temperatura acima do limite permitido.")  
