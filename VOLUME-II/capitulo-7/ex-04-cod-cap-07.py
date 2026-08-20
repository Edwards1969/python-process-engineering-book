# -*- coding: utf-8 -*-
"""

7.4.1 Sistemas de Segunda Ordem. - pág. 388

"""
import numpy as np
import matplotlib.pyplot as plt

# Simulação
def resposta_2a_ordem(t, k, zeta, wn):
	"""Calcula a resposta ao degrau para sistemas de 2a ordem."""
	if zeta < 1:
        
	# Subamortecido
		wd = wn * np.sqrt(1 - zeta**2)
		phi = np.arccos(zeta)
		y = k * (1 - (np.exp(-zeta * wn * t) / np.sqrt(1 - zeta**2)) * np.sin(wd * t + phi))
		return y
	elif zeta == 1:
        
		# Criticamente amortecido
		y = k * (1 - np.exp(-wn * t) * (1 + wn * t))
		return y
	else:
		# Superamortecido
		r1 = -wn * (zeta - np.sqrt(zeta**2 - 1))
		r2 = -wn * (zeta + np.sqrt(zeta**2 - 1))
		C1 = k * r2 / (r1 - r2)
		C2 = k * r1 / (r2 - r1)
		y = k + C1 * np.exp(r1 * t) + C2 * np.exp(r2 * t)
		return y
    
# Parâmetros de simulação
t = np.linspace(0, 20, 1000)
k = 1.0
wn = 1.0

# Diferentes cenários de zeta.
zetas = [0.2, 1.0, 2.5]
estilos = ['-', '--', ':']
labels = ['Subamortecido (zeta=0.2)', 
	'Criticamente Amortecido (zeta=1.0)', 
	'superamortecido (zeta=2.5)']

# Geração do gráfico para impressão.
plt.figure(figsize=(10,6))
for z, estilo, label in zip(zetas, estilos, labels):
	y = resposta_2a_ordem(t, k, z, wn)
	plt.plot(t, y, color='black', 
		linestyle=estilo,
		linewidth=1.5, 
		label=label) 
plt.axhline(y=1.0, color="black", linewidth=0.8, alpha=0.5)
plt.title("Resposta ao Degrau: Sistemas de Segunda Ordem")
plt.xlabel("Tempo (s)")
plt.ylabel("Saída y(t)")
plt.legend(loc="lower right")
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()
