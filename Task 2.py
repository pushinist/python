from collections import Counter
string = input().replace(" ", "")

cnt = Counter(string)

result = cnt.most_common(3)
for i in result:
    print(i[0], i[1])