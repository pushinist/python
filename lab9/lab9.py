import numpy as np

# with open("input.txt", 'w', encoding='utf-8') as f:
#     f.write('''3,4,17,-3
# 5,11,-1,6
# 0,2,-5,8''')
#
# with open('input.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     lines = list(map(lambda x: x.strip(), lines))
#     lines = list(map(lambda x: list(map(int, x.split(','))), lines))
#
# matrix = np.matrix(lines)
# print(matrix)
# summa = matrix.sum()
# print(summa)
# min_el = matrix.min()
# print(min_el)
# max_el = matrix.max()
# print(max_el)


# def rle(inputarray):
#     inarr = np.asarray(inputarray)
#     n = len(inarr)
#     if n == 0:
#         return None, None, None
#     else:
#         y = inarr[1:] != inarr[:-1]
#         i = np.append(np.where(y), n - 1)
#         z = np.diff(np.append(-1, i))
#         return inarr[i], z


#x = list(map(int, input().split(', ')))
#print(rle(x))
x = np.random.normal(size=(10, 4))
print(x)
print(f'Минимальное значение: {np.min(x)}, максимальное значение: {np.max(x)}, '
      f'среднее значение: {np.mean(x)}, стандартное отклонение: {np.std(x)}')
print(f'Первые 5 строк : \n {x[0:5]}')

