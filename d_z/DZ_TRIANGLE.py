class ValidTriang:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"Переменная '{self.__name}' должно быть положительным целым значением")
        instance.__dict__[self.__name] = value


class Triangle:
    a = ValidTriang()
    b = ValidTriang()
    c = ValidTriang()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def control_triang(self):
        if self.a + self.b > self.c and self.b + self.a > self.c and self.c + self.b > self.a:
            return f"Треугольник со сторонами ({self.a}, {self.b}, {self.c}) существует."
        else:
            return f"Треугольник со сторонами ({self.a}, {self.b}, {self.c}) не существует."


t1 = Triangle(2, 5, 6)
print(t1.control_triang())
t2 = Triangle(5, 2, 8)
print(t2.control_triang())
t3 = Triangle(7, 3, 6)
print(t3.control_triang())
