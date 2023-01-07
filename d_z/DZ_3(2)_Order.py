class ValidGoods:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"{self.__name} должно быть положительным значением")
        instance.__dict__[self.__name] = value


class Order:
    price = ValidGoods()
    quantity = ValidGoods()

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def sum_total(self):
        sum = self.price * self.quantity
        return sum


g1 = Order('apple', 5, 10)
print(f"Тест:\nOrder{g1.name, g1.price, g1.quantity}")
print()
print(g1.sum_total())

