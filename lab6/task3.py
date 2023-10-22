fin = open("input3.txt", 'r', encoding="utf-8")

min_age = 100
max_age = 0


for line in fin:
    if int((line.rstrip("\n").split())[-1]) > max_age:
        max_age = int((line.rstrip("\n").split())[-1])
        foutmax = open("output3max.txt", 'w', encoding="utf-8")
        foutmax.write(line)
        foutmax.close()
    elif int((line.rstrip("\n").split())[-1]) < min_age:
        min_age = int((line.rstrip("\n").split())[-1])
        foutmin = open("output3min.txt", 'w', encoding="utf-8")
        foutmin.write(line)
        foutmin.close()
    else:
        pass
