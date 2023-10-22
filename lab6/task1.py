def mult(arr):
    res = 1
    for item in arr:
        res *= item
    return res


fin = open("./lab6/input1.txt", "r")
arr = list(map(int, fin.readline().split()))
fin.close()

fout = open("./lab6/output1.txt", "w")
fout.write(str(mult(arr)))
fout.close()
