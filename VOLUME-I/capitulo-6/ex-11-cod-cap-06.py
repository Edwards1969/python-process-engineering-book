"""

Exemplo 2: Interpolação de Dados Experimentais.  -  pág. 158

"""
from scipy.interpolate import interp1d
import numpy as np

x = np.array([ 0, 1, 2, 3])
y = np.array([ 1.0, 2.7, 5.8, 6.6])

interp = interp1d(x, y, kind="linear")

print("y(1.5) = ", interp(1.5))