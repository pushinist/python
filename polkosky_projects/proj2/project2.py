import math
from typing import Tuple


class Vector:
    def __init__(self, x=0, y=0, z=0):
        if isinstance(x, (list, tuple)):
            self.x, self.y, self.z = x[:3]
        elif isinstance(x, int):
            self.x, self.y, self.z = x, y, z
        else:
            self.x, self.y, self.z = 0, 0, 0

    def __abs__(self):
        return self.length()

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    # Скалярное произведение
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'

    def __xor__(self, other):
        # Векторное произведение
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)

    @staticmethod
    def triple_product(a, b, c):
        # Смешанное произведение
        return a.dot_product(b ^ c)

    def __or__(self, other):
        # Проверка на коллинеарность
        return self ^ other == Vector(0, 0, 0)

    @staticmethod
    def are_complanar(a, b, c):
        # Проверка на компланарность
        return Vector.triple_product(a, b, c) == 0


# Пример использования класса Vector
v1 = Vector(2, 2, 0)
v2 = Vector(1, 1, 0)
v3 = Vector(7, 8, 9)

print(f"Вектор 1: {v1.x}, {v1.y}, {v1.z}")
print(f"Вектор 2: {v2.x}, {v2.y}, {v2.z}")
print(f"Вектор 3: {v3.x}, {v3.y}, {v3.z}")
print(f"Длина вектора 1: {abs(v1)}")
print(f"Вектор 1 + Вектор 2: {(v1 + v2).x}, {(v1 + v2).y}, {(v1 + v2).z}")
print(f"Вектор 2 - Вектор 1: {(v2 - v1).x}, {(v2 - v1).y}, {(v2 - v1).z}")
print(f"-Вектор 1: {(-v1).x}, {(-v1).y}, {(-v1).z}")
print(f"2 * Вектор 1: {(v1 * 2).x}, {(v1 * 2).y}, {(v1 * 2).z}")
print(f"Скалярное произведение Вектора 1 и Вектора 2: {v1.dot_product(v2)}")
print(f"Векторное произведение Вектора 1 и Вектора 2: {(v1 ^ v2).x}, {(v1 ^ v2).y}, {(v1 ^ v2).z}")
print(f"Смешанное произведение Вектора 1, Вектора 2 и Вектора 3: {Vector.triple_product(v1, v2, v3)}")
print(f"Вектор 1 и Вектор 2 коллинеарны: {v1 | v2}")
print(f"Вектор 1, Вектор 2 и Вектор 3 компланарны: {Vector.are_complanar(v1, v2, v3)}")
