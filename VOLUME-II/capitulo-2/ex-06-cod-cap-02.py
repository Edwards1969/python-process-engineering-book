# -*- coding: utf-8 -*-
"""

2.2.14 Impacto da Saturação e Zona Morta no Controle. - pág. 95

"""
import numpy as np
import matplotlib.pyplot as plt

def simulador_limites(u, u_min, u_max, delta):
	u_saida = np.copy(u)

	# Aplicando Zona Morta (Deadband)
	u_saida[np.abs(u_saida) < delta] = 0

	# Aplicando Saturacao
	u_saida = np.clip(u_saida, u_min, u_max)
	
	return u_saida

# Gerando um sinal de rampa para ver a transicao clara
u_sinal = np.linspace(-10, 110, 500) # Sinal de -10% a 110%

# Configurando limites: Zona Morta ate 10% e Saturacao em 90%
u_final = simulador_limites(u_sinal, u_min=0, u_max=90, delta=10)

# Plotagem Tecnica (Monocromatica)
plt.figure(figsize=(10, 6))
plt.plot(u_sinal, u_sinal, color='black', linestyle='--', label='Sinal Ideal (Sem Limites)')
plt.plot(u_sinal, u_final, color='black', linewidth=2, label='Sinal com Saturacao e Zona Morta')
plt.axhline(y=90, color='gray', linestyle=':', label='Limite de Saturacao (90%)')
plt.axvline(x=10, color='gray', linestyle=':', label='Fim da Zona Morta (10%)')
plt.title('Nao Linearidades: Efeito de Saturacao e Zona Morta')
plt.xlabel('Sinal Enviado pelo Controlador (%)')
plt.ylabel('Resposta Efetiva do Atuador (%)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
