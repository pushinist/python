import numpy as np

x = np.random.normal(size=(10, 4))
print(x)
print(f'Минимальное значение: {np.min(x)}, максимальное значение: {np.max(x)}, '
      f'среднее значение: {np.mean(x)}, стандартное отклонение: {np.std(x)}')
print(f'Первые 5 строк : \n {x[0:5]}')