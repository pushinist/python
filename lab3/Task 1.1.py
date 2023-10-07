string = input()

tmp_list = []

for i in range(1, len(string) - 1):
    if string[i] in '123456789':
        tmp_list.append(string[i - 1] * int(string[i]))
    else:
        if string[i + 1] in '123456789':
            pass
        else:
            tmp_list.append(string[i])

if string[-1] in '123456789':
    tmp_list.append(string[-2] * int(string[-1]))
else:
    tmp_list.append(string[-1])
    

print(*tmp_list, sep="")