'''
Модули

Создали файл с 2 функциями arithmetics.py по пути ./my_modules/arithmetics.py


from arithmetics import summator as summ # Импортируем одну функцию, как и ниже :)
from arithmetics import multiplicator as multi
import my_modules.bitwise as bitwise# Импортируем всю бибилотеку из внутренней директории

import arithmetics # Импортируем весь модуль из той же директории, в которой находится main.py
import my_modules.bitwise # Импортируем весь модуль из другой директории

import my_modules # Импортируем всю директорию, используем __init__.py в случае, если при импорте директории что-то нужно делать
from arithmetics import pi # Можно импортировать даже константы!!!


if __name__ == "__main__":
    b = map(int, input("Введите 2 числа: ").split())
    my_modules.arithmetics.summator(b)
    my_modules.arithmetics.multiplicator(b)
    my_modules.bitwise.bitwise_sum(b)
    my_modules.bitwise.bitwise_mult(b)
    print(pi)



print(b.__dict__)

if hasattr('max_level'):
    print(getattr('max_level'))

delattr('max_level')

class Car:
      def __init__(self, n, c, ml, fl, h = "False"):
            pass
            self.name = n
            self.color = c
            self.max_level = ml
            self.fuel_level = fl
            self.velocity = 0
            self.is_hybrid = h

      def add_fuel(self, x):
            if self.fuel_level + x > self.max_level:
                  self.fuel_level = self.max_level
            else:
                 self.fuel_level += x



a = Car()
a.name = "Toyota Land Cruiser"
a.fuel_level = 50
a.max_level = 100
print(a.name, a.color, a.max_level,
      a.fuel_level, a.is_hybrid)
b = Car()

print(b.name, b.color, b.max_level,
      b.fuel_level, b.is_hybrid)   
    

Car.name = "Auto"
Car.color = "Black"
Car.is_hybrid = True

c = Car()

print(a.name, a.color, a.max_level,
      a.fuel_level, a.is_hybrid)

print(b.name, b.color, b.max_level,
      b.fuel_level, b.is_hybrid) 

print(c.name, c.color, c.max_level,
      c.fuel_level, c.is_hybrid) 

Car.number = "123 АЯ"
print(a.__dict__)
b.name = "BNW"
b.color = "rainbow"
b.max_level = 70
b.is_hybrid = False
b.velocity = 100000

print(a.__dict__)
a.add_fuel(10)
print(a.__dict__)
a.add_fuel(10)
print(a.__dict__)
a.add_fuel(10)
print(a.__dict__)


a = Car("Mercedes", "Blue", 50, 20, True)
print(a.__dict__)

'''

class Vector:
      def __init__(self, x, y, z) -> None:
            self.x = x
            self.y = y
            self.z = z
      
      
      def __str__(self):
            return f"X : {self.x}; Y : {self.y}; Z : {self.z}"
        
      

      def __len__(self):
            return int((self.x ** 2 + self.y ** 2 + self.z ** 2) ** (1/2))
      

      def __add__(self, other):
            x3 = self.x + other.x
            y3 = self.y + other.y
            z3 = self.z + other.z
            return Vector(x3, y3, z3)
      

      def __mult__(self, other):
            if type(other) == Vector:
                  pass
            elif type(other) == int:
                  pass
            else:
                  return "Ты дурак"

a = Vector(1, -2, 5)
b = Vector(0, 4, -3)

c = a + b
print(c)
print(a)
print(len(a))
