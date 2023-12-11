x, y, z = map(int, input("Введите 3 числа: ").split())
if x == y and x == z:
    print("Совпало 3 числа")
elif x == y or x == z or z == y:
    print("Совпало 2 числа")
else:
    print("Совпало 0 чисел")
