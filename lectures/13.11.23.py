# import vectors
from vectors import Vector  # импортировали конкретный класс
from vectors import zero, ort_x, ort_y, ort_z
from vectors import StandardVectors  # самый лучший вариант
from vectors import A
import datetime as dt

a = Vector(1, 2, 3)
b = Vector(4, 5, 6)
print(a)
print(b)
c = a * ort_x
print(c)


class Human:
    def __init__(self, ln, fn, yb):
        self.lastname = ln
        self.firstname = fn
        self.year_of_birth = yb

    def get_age(self):
        return 2023 - self.year_of_birth

    def __str__(self):
        return f'{self.firstname} {self.lastname}, {self.year_of_birth} г'


class Student(Human):
    def __init__(self, ln, fn, yb, sp, gr):
        super().__init__(ln, fn, yb)
        self.specialization = sp
        self.grade = gr

    def __str__(self):
        return super().__str__() + \
            f', {self.grade} курс, {self.specialization}'


class Matob(Student):
    def __init__(self, ln, fn, yb, grade):
        super().__init__(ln, fn, yb, "МОАИС", grade)


a = Human(fn="Олег", ln="Полковский", yb=1987)
print(a)
b = Student(ln="Тарасов", fn="Дмитрий", yb=2004, sp="КБ", gr=2)
print(b)
c = Matob(fn="Кашапов", ln="Кирилл", yb=2004, grade=2)
print(c)


class A:
    def foo(self):
        print("Class A")

    def greet(self):
        print("hi, it's A")


class B:
    def bar(self):
        print("Class B")

    def greet(self):
        print("hi, it's b")


class C(A, B):
    def abc(self):
        print("Class abc")


c = C()

c.foo()
c.bar()
c.abc()
c.greet()

try:
    a = int(input())
    b = int(input())
    print(a / b)
except ValueError as e:
    print("Авария", e)
except ZeroDivisionError as e:
    print("Дели на ноль", e)
except Exception as e:
    print("Неизвестная ошибка", e)

try:
    a = int(input())
except:
    print("Ошибка")
else:
    print(a ** 2)
finally:
    print("Конец")


class RedGorilla(Exception):
    pass

def divider(apples, friends):
    if apples >= friends:
        return apples // friends
    else:
        raise RedGorilla("анлак")

try:
    print(divider(2, 4))
except Exception as e:
    print(e)

my_date = dt.date(2020, 11, 7)
print(my_date)
print(dt.date.today())
print(dt.date.today().weekday())
print(dt.datetime(2022, 12, 15, 13, 15, 9))
print(dt.datetime.now())
delta_time1 = dt.timedelta(seconds=10, weeks=2)
print(delta_time1)
print(delta_time1.days)
print(delta_time1.total_seconds())
print(dt.datetime.now().strftime("%B %Y-%m-%d"))
