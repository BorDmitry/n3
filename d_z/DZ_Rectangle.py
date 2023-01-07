from math import sqrt


class Rectangle:
    length = "0"
    width = "0"
    area = "0"
    perimeter = "0"
    hypotenuse = "0"

    def set_datos(selfs, length, width):
        if isinstance(length, int) and isinstance(width, int):
            selfs.length = length
            selfs.width = width
        else:
            print("Длина и ширина должны быть целыми числами")

    def get_datos(self):
        print(f"Длина прямоугольника: {self.length}\nШирина прямоугольника: {self.width}")

    def areas(self):
        s = self.length * self.width
        print("Площадь прямоугольника:", s)

    def perimeters(self):
        p = (self.length + self.width) * 2
        print("Периметр прямоугольника:", p)

    def hypotenuses(self):
        h = sqrt(self.length ** 2 + self.width ** 2)
        self.hypotenuse = h
        return print("Гипотенуза прямоугольника :", round(self.hypotenuse, 2))

    def drawing(self):
        for i in range(int(self.width)):
            print("*" * (int(self.length)), end="\n")


r1 = Rectangle()
r1.set_datos(9, 3)
r1.get_datos()
r1.areas()
r1.perimeters()
r1.hypotenuses()
r1.drawing()


# Длина прямоугольника: 9
# Ширина прямоугольника: 3
# Площадь прямоугольника: 27
# Периметр прямоугольника: 24
# Гипотенуза прямоугольника : 9.49
# *********
# *********
# *********
#
# Process finished with exit code 0
