"""

4.6.7 Trajetória de uma partícula em 3D - pág. 96

"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 20, 500)

x = np.cos(t)
y = np.sin(t)
z = 0.1*t

fig = plt.figure(figsize=(8,5), facecolor='white')

ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, color='black', linewidth=2)
ax.set_title('Trajetória de um Particular')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.set_xticks(np.linspace(-1,1,5))
ax.set_yticks(np.linspace(-1,1,1))
ax.set_zticks(np.linspace(0,2,5))

plt.show()

