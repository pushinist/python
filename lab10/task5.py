import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def calculate_mse(x, y):
    return np.mean((x - y)**2)

x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(2 * np.pi * X) * np.cos(2 * np.pi * Y)  # Пример функции

mse_values = np.zeros_like(Z)
for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        mse_values[i, j] = calculate_mse(Z[i, j], np.zeros_like(Z[i, j]))


fig = plt.figure(figsize=(10, 5))

ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, mse_values, cmap='viridis')
ax1.set_title('MSE (обычный масштаб)')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('MSE')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, mse_values, cmap='viridis')
ax2.set_title('MSE (логарифмический масштаб)')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('MSE')
ax2.set_yscale('log')  

plt.tight_layout()
plt.show()
