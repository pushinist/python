import functools
'''
Парадигмы 

Императивная (как сделать?) + Декларативная (что мы получим в результате?)


Примеры императивной - стукрутрное программирование, ООП
Примеры декларативной - функциональное программирование (Lisp умер 😭)


Фишки функционального программирования:
1) долой переменные, ура функциям
2) долой циклы, ура рекурсиям

'''


# lambda анонимные функции
a = lambda x, y: x + y
print(a(2, 3))
#Output: 5

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map(func, iterable object) - применяет ф-ию к каждому item итерируемого объекта, на выходе получаем map object
aboba = map(str, A)
print(aboba)
# filter(func, iterable object) - сортирует коллекцию по каким-то параметрам, заданным в фунцкии, на выходе получаем filter object
abobus = filter(lambda x: x % 2 == 0, A)
print(abobus)
# reduce(func, iterable object) - применяется там, где нужно вернуть число
abingus = functools.reduce(lambda x, y: x + y, A) # складывает все числа в списке
print(abingus)

# zip - объединяет (последовательности), возвращает объект типа zip
l = [1, 2, 3]
m = 'abc'
n = [True, False]
autobus = zip(l, m, n)

print(autobus)


'''
##############################################################################################
                                ООП

Абстракция - база, выделение главного, отказ от мелочей
Полиморфизм - возможность нескольких реализаций одной идеи
Инкапсуляция - public только то что должно быть public, про безопасность
Наследование - новые объекты на основе свойств старых

плюс ООП:
возможность переиспользования кода

минус ООП:
сложночитаемый код
дольше писать чем в структурном подходе
algol, simula, smalltalk

На практике рассмотрим модуль tkinter

'''

class Student:
    def __init__(self, name, univ = 'Default Univ', state = False):
        self.name = name # динамическое поле (изменяемое)
        self.univ = univ # динамическое поле (изменяемое)
        self.state = state # динамическое поле (изменяемое)
    
    
    def append(self):
        self.state = True
    

alex = Student("Alex")
print(alex.state) # Output - False
alex.append()
print(alex.state) # Output - True


# Наследование
class Animal:
    def make_sound(self):
        print("Издает звук")



class Cat(Animal):
    def dropall(self):
        print('Все упало')
    
    
    def make_sound(self):
        return super().make_sound()
        


class Kitten(Cat):
    def die(self):
        print('Умер')

kit = Kitten()
kit.make_sound() 
kit.dropall()
kit.die()