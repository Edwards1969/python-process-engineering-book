# -*- coding: utf-8 -*-
"""

7.4.1 Sistemas de Primeira Ordem. - pág. 388

"""
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Parâmetros do sistema de primeira ordem (sensor térmico)
# ============================================================
K = 1.0            # Ganho estático
tau = 15.0         # Constante de tempo (s)
T_inicial = 25.0   # Temperatura inicial (°C)
T_final = 100.0    # Degrau aplicado (°C)
A = T_final - T_inicial  # Amplitude do degrau

# ============================================================
# Vetor de tempo
# ============================================================
t = np.linspace(0, 80, 500)

# ============================================================
# Resposta ao degrau: y(t) = Ti + K*A*(1 - exp(-t/tau))
# ============================================================
y = T_inicial + K * A * (1 - np.exp(-t / tau))

# Valor teórico em t = tau (63,2% da subida)
y_tau = T_inicial + 0.632 * A

# ============================================================
# Gráfico
# ============================================================
plt.figure(figsize=(9, 5))
plt.plot(t, y, color='black', linewidth=2, label='Resposta do Sensor')

# Linha horizontal do valor final
plt.axhline(y=T_final, color='black', linestyle=':', linewidth=1, alpha=0.7)

# Linha vertical em t = tau
plt.axvline(x=tau, color='black', linestyle='--', linewidth=1, alpha=0.7)

# Ponto em t = tau
plt.scatter([tau], [y_tau], color='black', zorder=5)

# Anotação
plt.annotate(
	f't = tau ({tau:.0f} s)\n63,2% da resposta',
	xy=(tau, y_tau),
	xytext=(tau + 5, y_tau - 10),
	arrowprops=dict(arrowstyle='->', color='black')
)
plt.title('Resposta ao Degrau: Sistema de Primeira Ordem (Sensor Térmico)')
plt.xlabel('Tempo (s)')
plt.ylabel('Temperatura (°C)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()

# Conferência no console
print(f"Temperatura em t = tau: {y_tau:.2f} °C")

