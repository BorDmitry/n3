from math import sqrt


class Shape:
    def __init__(self, color: str = 'red'):
        self.color = color

    def perimetr(self):
        raise NotImplementedError("В дочернем классе должен быть определён метод perimetr()")

    def area(self):
        raise NotImplementedError("В дочернем классе должен быть определён метод area()")

    def info(self):
        raise NotImplementedError("В дочернем классе должен быть определён метод info()")

    def draw(self):
        raise NotImplementedError("В дочернем классе должен быть определён метод draw()")


class Square(Shape):
    def __init__(self, color, a):
        super().__init__(color)
        self.a = a

    def area(self):
        area = self.a * self.a
        return area

    def perimetr(self):
        perimetr = 4 * self.a
        return perimetr

    def info(self):
        print()
        print(f'===Квадрат===\nСторона: {self.a}\nЦвет: {self.color}\n'
              f'Площадь: {self.area()}\nПериметр: {self.perimetr()}')

    def draw(self) -> None:
        for i in range(self.a):
            print("*" * self.a)
        print()


class Rectangle(Shape):
    def __init__(self, color, h, w):
        super().__init__(color)
        self.h = h
        self.w = w

    def area(self):
        area = self.h * self.w
        return area

    def perimetr(self):
        perimetr = 2 * (self.h + self.w)
        return perimetr

    def info(self):
        print(f'===Прямоугольник===\nДлина: {self.h}\nШирина: {self.w}\nЦвет: {self.color}\n'
              f'Площадь: {self.area()}\nПериметр: {self.perimetr()}')

    def draw(self) -> None:
        for i in range(self.w):
            print("*" * self.h)
        print()


class Triangle(Shape):
    def __init__(self, color, a, b, c):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        h = sqrt(self.b ** 2 - (self.a / 2) ** 2)
        area = round(0.5 * self.a * h, 2)
        return area

    def perimetr(self):
        perimetr = self.a + self.b + self.c
        return perimetr

    def info(self):
        print(f'===Треугольник===\nСторона 1: {self.a}\nСторона 2: {self.b}\nСторона 3: {self.c}\n'
              f'Цвет: {self.color}\nПлощадь: {self.area()}\nПериметр: {self.perimetr()}')

    def draw(self) -> None:
        count1 = 1
        count2 = self.a / 2
        for i in range(self.b):
            print(" " * int(count2), "*" * count1)
            count1 += 2
            count2 -= 1


s1 = Square("red", 3)
r1 = Rectangle("green", 7, 3)
t1 = Triangle("yellow", 11, 6, 6)
shape = [s1, r1, t1]
for g in shape:
    g.info(), g.draw()


