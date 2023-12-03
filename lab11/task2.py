import numpy as np
import matplotlib.pyplot as plt


plt.hist(172 + 8 * np.random.randn(10000), 100, facecolor="blue")
plt.title('Нормальное распределение')
plt.xlabel('Величина')
plt.ylabel('Плотность вероятности')
plt.show()



