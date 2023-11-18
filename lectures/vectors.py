class Vector:
    def __init__(self, x0, y0, z0):
        self.x = x0
        self.y = y0
        self.z = z0

    def __init__(self, x0 = None, y0 = None, z0 = None):
        if (x0 is None) and (y0 is None) and (z0 is None):
            self.x = 0
            self.y = 0
            self.z = 0
        elif x0 is not None:
            if type(x0) is list or type(x0) is tuple:
                self.x = x0[0]
                self.y = x0[1]
                self.z = x0[2]
            elif type(x0) is int:
                self.x = x0
                self.y = x0
                self.z = x0


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __neq__(self, other):
        return not (self == other)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (1 / 2)

    def __iadd__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        if type(other) is Vector:
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            return Vector(self.x * other, self.y * other, self.z * other)

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __getitem__(self, other):
        return

    def _contains(self, other):
        if type(other) is Vector:
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return self.x == other and self.y == other and self.z == other

    def vector_product(a, b):
        x3 = a.y * b.z - a.z * b.y
        y3 = a.y * b.z + a.z * b.y
        z3 = a.y * b.z - a.z * b.y

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == 1:
            return self.x
        elif self.counter == 2:
            return self.y
        elif self.counter == 3:
            return self.z
        else:
            raise StopIteration




zero = Vector(0, 0, 0)
ort_x = Vector(1, 0, 0)
ort_y = Vector(0, 1, 0)
ort_z = Vector(0, 0, 1)
class StandardVectors:
    zero = Vector(0, 0, 0)
    ort_x = Vector(1, 0, 0)
    ort_y = Vector(0, 1, 0)
    ort_z = Vector(0, 0, 1)


A = [Vector(0, 0, 0),
     Vector(1, 0, 0),
     Vector(0, 1, 0),
     Vector(0, 0, 1)]
