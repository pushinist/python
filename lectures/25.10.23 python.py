'''
Итераторы & Генераторы 

num = [1, 2, 3, 4, 5]
sqn = (num ** 2 for num in num)

print(type(sqn)) # Получаем генератор
ls = list(sqn)
print(ls)

ls1 = list(sqn)
print(ls1) # Получили пустой список, -> генератор - одноразовый прикол

print(4 in sqn) # True
print(4 in sqn) # False

ls = [1, 2, 3]

j = 0


for j in ls:
    print(j)

# аналог for j in ls:
while j < len(ls):
    print(ls[j])
    j += 1

    

s = '123'
l = [1, 2, 3]
m = {1, 2, 3}

# Получили итераторы 
print(iter(s))
print(iter(l))
print(iter(m))

m_it = iter(m)

print(next(m_it)) 
print(next(m_it))
print(next(m_it))



class Series(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high
        
    
    def __iter__(self):
        return self


    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current = 1
            return self.current - 1


import sys
import itertools

ls1 = [4] * 10_000_000
print(sys.getsizeof(ls1))
print(type(ls1)) # Обычный список
ls2 = itertools.repeat(4, 10_000_000)
print(type(ls2)) # объект itertools.repeat
print(sys.getsizeof(ls1) // sys.getsizeof(ls2)) # Объект занимает в полтора миллиона раз меньше памяти


f = open('aboba.txt', 'w')
for i in f: # итерация по строкам O_O
    pass

from itertools import count


for i in count(): # Бесконечный индекс for (что?????????)
    print(i) 



Г Е Н Е Р А Т О Р Ы O_O    

ls = [1, 2, 3, 4, 5]
sqn = (num ** 2 for num in ls) # Выражение-генератор

def f_sqn(numbers_lst):
    for n in numbers_lst:
        yield n ** 2 # yield - ключевое слово, указывающие на функцию-генератор
    print(next(f_sqn))


def getfour():
    yield 4

get4 = getfour()
print(get4) # Объект, чтобы получить непосредственно значение, нужно вытаскивать его через метод next()
print(next(get4)) # вотъ этоть    

class Count(): # Объект-генератор
    def __init__(self, start = 0):
        self.num = start

    
    def __iter__(self):
        return self
    

    def __next__(self):
        num = self.num
        self.num += 1
        return num

        

def count(start = 0): # Функция-генератор
    num = start
    while True:
        yield num
        num += 1


c = count()
print(next(c)) # == 0
print(next(c)) # == 1, и т.д.

for i in count(): # еще один бесконечный for O_O
    print(i)



'''
