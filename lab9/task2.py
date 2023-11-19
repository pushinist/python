import numpy as np

def rle(inputarray):
    inarr = np.asarray(inputarray)
    n = len(inarr)
    if n == 0:
        return None, None, None
    else:
        y = inarr[1:] != inarr[:-1]
        i = np.append(np.where(y), n - 1)
        z = np.diff(np.append(-1, i))
        return inarr[i], z
    
x = list(map(int, input().split(', ')))
print(rle(x))