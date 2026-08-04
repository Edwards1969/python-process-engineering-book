"""

6.7.10 Exercício 1: Cálculo da Área sob uma Curva Experimental. - pág. 184

"""
import numpy as np
from scipy.integrate import trapezoid

# Dados amostrados (Tempo em segundos, sinal em Volts).
tempo = np.array([0, 1, 2, 3, 4, 5])
sinal = np.array([0.0, 1.2, 2.5, 2.0, 1.0, 0.3])

# Cálculo da eneergia acumulada (Integral numérica)
energia = trapezoid(sinal, tempo)

print(f"Energia Total Estimada: {energia:.4f} Joules")

"""
Comentário didático:

Explicação sobre o uso de trapezoid(sinal, tempo):

A função trapezoid do SciPy implementa a Regra do Trapézio para calcular
integrais numéricas. Sua assinatura é:

    trapezoid(y, x)

onde:
    x → vetor das abscissas (eixo horizontal)
    y → vetor das ordenadas (eixo vertical)

No nosso caso:
    tempo = x  (domínio da função)
    sinal = y  (valores da função)

Portanto, trapezoid(sinal, tempo) calcula a integral:

    ∫ sinal(t) dt

que representa a energia acumulada do sinal ao longo do tempo.

Se invertêssemos a ordem, trapezoid(tempo, sinal), estaríamos calculando:

    ∫ tempo(sinal) d(sinal)

o que não faz sentido físico para este problema.

Resumo:
- tempo é o eixo x
- sinal é o eixo y
- trapezoid(y, x) = integral de y em relação a x
"""
