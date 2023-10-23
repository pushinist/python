'''
Модули

Создали файл с 2 функциями arithmetics.py по пути ./my_modules/arithmetics.py


from arithmetics import summator as summ # Импортируем одну функцию, как и ниже :)
from arithmetics import multiplicator as multi
import my_modules.bitwise as bitwise# Импортируем всю бибилотеку из внутренней директории

import arithmetics # Импортируем весь модуль из той же директории, в которой находится main.py
import my_modules.bitwise # Импортируем весь модуль из другой директории


'''
import my_modules # Импортируем всю директорию, используем __init__.py в случае, если при импорте директории что-то нужно делать
from arithmetics import pi # Можно импортировать даже константы!!!


if __name__ == "__main__":
    a, b = map(int, input("Введите 2 числа: ").split())
    my_modules.arithmetics.summator(a, b)
    my_modules.arithmetics.multiplicator(a, b)
    my_modules.bitwise.bitwise_sum(a, b)
    my_modules.bitwise.bitwise_mult(a, b)
    print(pi)