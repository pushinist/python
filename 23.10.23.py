'''
Модули

Создали файл с 2 функциями arithmetics.py по пути ./my_modules/arithmetics.py
'''
import arithmetics as arith # Импортируем всю бибилотеку
from arithmetics import summator as summ # Импортируем одну функцию, как и ниже :)
from arithmetics import multiplicator as multi
from arithmetics import pi # Можно импортировать даже константы!!!

if __name__ == "__main__":
    a, b = map(int, input("Введите 2 числа: ").split())
    summ(a, b)
    multi(a, b)
    print(pi)