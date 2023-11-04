# Декораторы
'''
def my_decor(func):
    def wrapper(a, b):
        print('Прелюдия')
        print(func(a, b))
        print('Занавес')
        return
    return wrapper


def summa(x, y):
    return x + y


my_new_sum = my_decor(summa)

my_new_sum(10, 20)


def protection(password):
    def decor(func):
        pwd = input('Введите пароль:')
        if pwd == password:
            def wrapper(a, b):
                print('А')
                print(func(a, b))
                print('боба')
            return wrapper
        else:
            def default(a, b):
                print('нуб.')
            return default
    return decor

@protection("12345aboba")
def summa(x, y):
    return x + y


summa(10, 20)
summa(50, 60)
# Чтение файлов

A = [1, 2, 78, 10, 255, 0, 123, 31]
print(type(A))
B = bytes(A)
print(type(B))
print(B)
print(len(B))
for x in B:
    print(x)

C = list(B)

fout = open("output.bin", "wb")
fout.write(B)
fout.close()

x = 874521
A = []
while x > 0:
    A.append(x % 256)
    x //= 256
print(A)
B = bytes(A)

s = 'абоба'
A = []
for x in s:
    A.append(ord(x))
print(A)

C = [x]
for x in A:
    C.append(x % 256)
    C.append(x // 256)


A = [
    ("Чипсы", 95, 12),
    ("Огурцы", 70, 5),
    ("Помидоры", 110, 2)    
]

B = "Чипсы".encode("utf-8")
print(B)
print(len(B))

fout = open("output.bin", "wb")

n = len(A)
B = n.to_bytes(4, "little")
fout.write(B)

for x in A:
    item = x[0]
    price = x[1]
    quantity = x[2]
    
for item, price, quantity in A: # Аналог тому, что выше    
    B = item.encode("utf-8")
    size = len(B)
    C = size.to_bytes(4, "little")
    fout.write(C)
    fout.write(B)
    
    C = price.to_bytes(4, "little")
    fout.write(C)
    
    C = quantity.to_bytes(4, "little")
    fout.write(C)
    
fout.close()

print(A)

fin = open("output.bin", "br")

B = fin.read(4)
n = int.from_bytes(B, "little")
for _ in range(n):
    C = fin.read(4)
    size = int.from_bytes(C, "little")
    B = fin.read(size)
    s = str(B, "utf-8")


    B = fin.read(4)
    price = int.from_bytes(B, "little")
    
    B = fin.read(4)
    quantity = int.from_bytes(B, "little")
    
    print(s, price, quantity)
fin.close()

import struct # все что делали выше есть тут и оно проще!!!!!!!!!!!🔥🔥🔥🔥🔥🔥🔥

'''



'''
Работа с текстом O_O

'''

'''


line = fin.readline() # Считывает 1 строку
print(line)

# Считать все строчки у текстовика
while True:
    s = fin.readline().rstrip("\n")
    if s == '':
        break


# Для бинарников
while True:
    B = fin.read(1)
    if B == b"":
        break
# Еще один способ считать все строки
for line in fin:
    s = line.rstrip("\n")
    print(s)


print(fin.read(7)) # Считал 7 первых символов, потому что fin считается текстовиком, т.к. не указали в атрибутах, что он бинарник


#Запись в файлы

fin = open("Анечка.txt", "r", encoding="utf-8")

fin.close()

fout = open("Лабуда.txt.", "w", encoding="utf-8")
fout.write("ABOBUS ")
fout.write("1245") # инты в кавычках, иначе дропнет ошибку 😈
fout.write("\n")

print("Привет", 1256, 1.25, file=fout, sep="\n") # то же самое, только все быстро в одну строчку и гигахайп

fout.close()

# Распаковка списка в файл

A = [
    ("Чипсы", 95, 12),
    ("Огурцы", 70, 5),
    ("Помидоры", 110, 2)    
]

fout = open("aboba.txt", "w")
for item, price, quantity in A:
    print(item, price, quantity, file=fout)

fout.close()

# Обратно
fin = open("Анечка.txt", "r")
for line in fin:
    s = line.rstrip("\n")
    item, price, quantity = s.split()
    price = int(price)
    quantity = int(quantity)
    print(item, price, quantity)
fin.close()


# Как не писать метод close()


A = [
    ("Чипсы", 95, 12),
    ("Огурцы", 70, 5),
    ("Помидоры", 110, 2)    
]


with open("abobus.txt", "w") as fout:
    for item, price, quantity in A:
        print(item, price, quantity, file=fout)



'''
