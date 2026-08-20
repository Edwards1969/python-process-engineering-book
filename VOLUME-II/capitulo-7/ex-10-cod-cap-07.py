# -*- coding: utf-8 -*-
"""

7.6.1 Controle por Realimentação (Feedback). pág. 422
Exemplo Prático: Controle de Nível em um Tanque de Armazenamento - pág.423

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
# 1. Parâmetros do sistema
Kp = 5.0          # Ganho proporcional
tau = 10.0        # Constante de tempo do processo (s)
K_processo = 1.0  # Ganho do processo
# 2. Função de Transferência do Processo G(s) = 1 / (10s + 1)
num_g = [K_processo]
den_g = [tau, 1]
sys_g = signal.TransferFunction(num_g, den_g)
# 3. Função de Transferência em Malha Fechada Gmf(s) = 5 / (10s + 6)
num_mf = [Kp]
den_mf = [tau, 1 + Kp]
sys_mf = signal.TransferFunction(num_mf, den_mf)
# 4. Simulação da resposta ao degrau unitário
t = np.linspace(0, 50, 500)
t, y = signal.step(sys_mf, T=t)
# 5. Cálculo automático do valor de regime e erro
y_ss = Kp / (1 + Kp)          # Valor final teórico (5/6)
erro_ss = 1 - y_ss            # Erro de regime permanente
# 6. Gráfico
plt.figure(figsize=(8, 5))
plt.plot(t, y, color='black', linewidth=1.5,
label=f'Resposta Realimentada (Kp={Kp})')
plt.axhline(y=1.0, color='black', linestyle=':',
label='Setpoint Desejado')
plt.axhline(y=y_ss, color='black', linestyle='--', alpha=0.5,
label=f'Valor de Regime ({y_ss:.3f})')
plt.title('Controle de Nível com Realimentação Proporcional')
plt.xlabel('Tempo (s)')
plt.ylabel('Nível do Tanque (m)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
# 7. Impressão dos resultados numéricos
print(f"Valor final da simulação: {y[-1]:.4f}")
print(f"Valor teórico de regime: {y_ss:.4f}")
print(f"Erro de regime permanente: {erro_ss:.4f} ({erro_ss*100:.1f}%)")



