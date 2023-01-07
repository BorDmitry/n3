class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")

        self.sec = sec % self.__DAY

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec + other.sec)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError()
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError()
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError()
        return Clock(self.sec % other.sec)

    def __eq__(self, other):
        return self.sec == other.sec

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.sec > other.sec

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")

        if item == "hour":
            return (self.sec // 3600) % 24
        elif item == "min":
            return (self.sec // 60) % 60
        elif item == "sec":
            return self.sec % 60
        return "Неверный ключ"

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Ключ должен быть строкой")
        if not isinstance(value, int):
            raise ValueError("Значение должно быть целым числом ")
        s = self.sec % 60              # секунды
        m = (self.sec // 60) % 60      # минуты
        # h = (self.sec // 3600) % 24    # часы
        if key == "hour":
            self.sec = s + 60 * m + value * 3600
        # elif key == "min":
        #     self.sec = s + 60 * value + h * 3600
        # elif key == "sec":
        #     self.sec = value + 60 * m + h * 3600


c1 = Clock(80000)
print(c1.get_format_time())
c1["hour"] = 10
print(c1["hour"], c1["min"], c1["sec"])

c1["hour"] = 8
print(c1.get_format_time())
print(c1["hour"], c1["min"], c1["sec"])

