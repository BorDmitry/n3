class Point3D:
    CH = "Координаты должна быть числом"
    RIGHT = "Правый операнд должен быть типом данных Point3D"

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):                                   # для просмотра  координат вспомогательного класса Point3D
        return f'{self.__x}, {self.__y}, {self.__z}'

    @staticmethod
    def __chek_value(v):
        return isinstance(v, int) or isinstance(v, float)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.__chek_value(value):
            self.__x = value
        else:
            print(self.CH)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.__chek_value(value):
            self.__y = value
        else:
            print(self.CH)

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, value):
        if self.__chek_value(value):
            self.__z = value
        else:
            print(self.CH)

    def __add__(self, other):
            if not isinstance(other, Point3D):
                raise ValueError(self.RIGHT)
            return Point3D(self.__x + other.x, self.__y + other.y, self.__z + other.z)

    def __sub__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError(self.RIGHT)
        return Point3D(self.__x - other.x, self.__y - other.y, self.__z - other.z)

    def __mul__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError(self.RIGHT)
        else:
            return Point3D(self.__x * other.x, self.__y * other.y, self.__z * other.z)

    @staticmethod
    def __check0(exemplar):
        if exemplar.x == 0 or exemplar.y == 0 or exemplar.z == 0:
            raise ZeroDivisionError("Ни одна из коорд второго операнда не должна быть равна 0")

    def __truediv__(self, other):
        if not isinstance(other, Point3D):
            raise ValueError(self.RIGHT)
        self.__check0(other)
        return Point3D(self.__x / other.x, self.__y / other.y, self.__z / other.z)

    def __eq__(self, other):
        if not isinstance(other, Point3D):
            raise ValueError(self.RIGHT)
        return self.__x == other.x and self.__y == other.y and self.__z == other.z

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")
        elif item == "x":
            return self.__x
        elif item == "y":
            return self.__y
        elif item == "z":
            return self.__z
        else:
            print("Неверно задан ключ")

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Ключ д б строкой")
        if self.__chek_value(value):
            if key == 'x':
                self.__x = value
            elif key == 'y':
                self.__y = value
            elif key == 'z':
                self.__z = value
            else:
                print("Координаты д б числом")


pt1 = Point3D(12, 15, 18)
pt2 = Point3D(6, 3, 9)
print("Координаты первой точки:", pt1)
print("Координаты второй точки:", pt2)


pt3 = pt1 + pt2
print(f'Сложение кординат: ({pt3})')
pt4 = pt1 - pt2
print(f'разность коорд.:, ({pt4})')

pt5 = pt1 * pt2
print(f'умножение коорд.:, ({pt5})')

pt6 = pt1 / pt2
print(f'частное коорд.:, ({pt6})')

print(f'Равенство координат:', pt1 == pt2)


print("x=", pt1['x'], "x1=", pt2['x'])
print("y=", pt1['y'], "y1=", pt2['y'])
print("z=", pt1['z'], "z1=", pt2['z'])

pt1['x'] = 20
print("Запись значения в координату х:", pt1['x'])

