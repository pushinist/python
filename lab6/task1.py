def mult(arr):
    res = 1
    for item in arr:
        res *= item
    return res


fin = open("input1.txt", "w")
fin.write("1 2 3 4 5 6 7 8 9 10")
fin.close()

fin = open("input1.txt", "r")
arr = list(map(int, fin.readline().split()))
fin.close()

fout = open("output1.txt", "w")
fout.write(str(mult(arr)))
fout.close()







fin.close
