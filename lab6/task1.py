def mult(arr):
    res = 1
    for item in arr:
        res *= item
    return res


fin = open("input.txt", "w")
fin.write("1 2 3 4 5 6 7 8 9 10")
fin.close()

fin = open("input.txt", "r")
arr = list(map(int, fin.readline().split()))
fin.close()

fout = open("output.txt", "w")
fout.write(str(mult(arr)))
fout.close()







fin.close
