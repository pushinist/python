fin = open("input2.txt", "r")
arr = []
for line in fin:
    arr.append(int(line.rstrip("\n")))

arr.sort()
print(arr)

fout = open("output2.txt", "w")
for item in arr:
    print(item, sep="\n", file=fout)

fout.close()

