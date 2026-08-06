"""

8.2 Amostragem e Discretização de Sinais. - pág. 229-231

Exemplo Numérico: Monitoramento de Vibração.

"""
import numpy as np
import matplotlib.pyplot as plt

f_sinal = 60
t_final = 0.1
t_analogico = np.linspace(0, t_final, 1000)
sinal_analogico = np.sin(2 * np.pi * f_sinal * t_analogico)

fs = 600
dt = 1/fs
t_digital = np.arange(0, t_final, dt)
sinal_digital = np.sin(2 * np.pi * f_sinal * t_digital)

plt.figure(figsize=(10, 4))
plt.plot(t_analogico, sinal_analogico, label="Sinal Analógico", alpha=0.5)
plt.stem(t_digital, sinal_digital, 'r', label=f"Amostras ({fs} Hz)" )
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()