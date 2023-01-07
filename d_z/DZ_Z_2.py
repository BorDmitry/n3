class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'({self.__x}, {self.__y})'


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width


class Line(Prop):
    def draw_line(self):
        print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')

    def set_coords(self, sp: Point, ep: Point):
        if not isinstance(sp, int) or not isinstance(ep, int):
            print("Координаты должны быть целочисленными")
        else:
            self._sp = sp
            self._ep = ep


class Rect(Prop):
    def draw_rect(self):
        print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')



line = Line(Point(1, 2), Point(10, 20))
line.draw_line()

line.set_coords(Point(10.2, 20), Point(100, 200))
line.draw_line()
print()
rect = Rect(Point(7, 9), Point(12, 15))
rect.draw_rect()

rect = Rect(Point(30.5, 40.2), Point(50, 60))
rect.draw_rect()
