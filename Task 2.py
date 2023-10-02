from collections import Counter
string = 'aabbbbaasdqweqwekajfkmbsdjfnsajkdfhajdskvnlsd vauh dsahfajksdnfksadjf'.replace(" ", "")

cnt = Counter(string)
dict(cnt)
print(cnt)
maximum = max(cnt, key=cnt.get)
print(maximum, cnt[maximum])