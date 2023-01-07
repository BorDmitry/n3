class Liquid:
    def __init__(self, name, density):
        self._name = name
        self._density = density

    def change_density(self, val):
        self._density = val

    def calc_v(self, m):
        v = m / self._density
        print(f'Объём {m} кг {self._name} равен {v} m^3.')

    def calc_m(self, v):
        m = self._density * v
        print(f'Вес {v} m^3 of {self._name} состовляет {m} кг')

    def print_info(self):
        print(f"Жидкость '{self._name}' (плотность = {self._density} kg/m^3).")


class Alcohol(Liquid):
    def __init__(self, name, density, strength):
        super().__init__(name, density)
        self.strength = strength

    def change_strength(self, val):
        self.strength = val


a = Alcohol('Wine', 1064.2, 14)
a.print_info()

a.change_density(1000)
a.print_info()

a.calc_m(0.5)
a.calc_v(300)

print(a.strength)
a.change_strength(20)
print(a.strength)



