"""
4.2.6 Subplots - pág. 67

"""
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, 200)
y1 = np.sin(t)
y2 = np.cos(t)

plt.subplot(2,1,1)
plt.plot(t, y1, color="black", linewidth=2)
plt.title("Seno")

plt.subplot(2,1,2)
plt.plot(t, y2, color="black", linewidth=2)
plt.title("Cosseno")

plt.tight_layout()
plt.show()