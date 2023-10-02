string = input()
counter = 1
tmp_list = []

for i in range(1, len(string)):
    if string[i] == string[i - 1]:
        counter += 1
    else:
        if counter != 1:
            tmp_list.append(string[i - 1] + str(counter))
            counter = 1
        else:
            tmp_list.append(string[i - 1])

if counter == 1:
    tmp_list.append(string[-1])
else:
    tmp_list.append(string[i - 1] + str(counter))

print(string)
print(*tmp_list, sep="") 