import numpy as np

with open("input.txt", 'w', encoding='utf-8') as f:
     f.write('''3,4,17,-3
5,11,-1,6
0,2,-5,8''')

with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    lines = list(map(lambda x: x.strip(), lines))
    lines = list(map(lambda x: list(map(int, x.split(','))), lines))

matrix = np.matrix(lines)
print(matrix)
summa = matrix.sum()
print(summa)
min_el = matrix.min()
print(min_el)
max_el = matrix.max()
print(max_el)