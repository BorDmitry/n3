class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix1 = 'EUR'
    suffix2 = 'USD'

    def __init__(self, num, surname, percent, value=0):
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.__value = value
        print(f'Счёт #{self.__num} принадлежит {self.__surname} был открыт.')
        print('*' * 50)

    @property
    def num(self):
        return self.__num

    @ num.setter
    def num(self, n):
        if isinstance(n, int):
            self.__num = n
        else:
            print("Для ввода номера счёта введите целочисленнные значения")

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, s):
        if isinstance(s, str):
            self.__surname = s
        else:
            print("Для ввода имени владельца введите буквенные значения")

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, p):
        if isinstance(p, (int, float)):
            self.__percent = p
        else:
            print("Для ввода новых процентов введите вещественные значения")

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        if isinstance(v, int):
            self.__value = v
        else:
            print("Для ввода суммы введите целочисленнные значения")

    def __del__(self):
        print('*' * 50)
        print(f'Счёт #{self.num} был закрыт.')

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate


    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счёта в USD: {usd_val} {Account.suffix2}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f'Состояние счёта в EUR: {eur_val} {Account.suffix1}')

    def print_balance(self):
        print(f'Текущий баланс {self.__value} {Account.suffix}')
    #
    def print_info(self):
        print(f'Инф о счёте')
        print('-' * 20)
        print(f'#{self.__num}')
        print(f'Владелец {self.__surname}')
        self.print_balance()
        print(f'Проценты: {self.__percent:.0%}')
        print('-' * 20)

    def add_percents(self):
        self.__value += self.__value * self.__percent
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f'К сожалению Вы не можете снять {val}')
        else:
            self.__value -= val
            print(f'{val} RUB было успешно снято')
            self.print_balance()

    def add_money(self, val):

        self.__value += val
        print(f'{val} RUB было добавлено')


acc = Account('12345', 'Долгих', 0.03, 1000)

acc.print_info()

acc.num = 56789
print(f'#{acc.num} > Новый номер счёта присвоен')

acc.surname = "Ботвинник"
print(f'Новый владелец счёта объявлен: {acc.surname}')

acc.percent = 0.05
print(acc.percent, "> Процентная ставка установлена")

acc.value = 100000
print(acc.value, "> Текущий баланс объявлен")
print()
acc.print_info()

acc.convert_to_usd()
acc.convert_to_eur()
print()
Account.set_usd_rate(2)
acc.convert_to_usd()
print()
Account.set_eur_rate(3)
acc.convert_to_eur()
print()
acc.add_percents()

acc.withdraw_money(3000)
print()
acc.print_balance()
print()
acc.add_money(5000)
print()
acc.print_balance()
print()
acc.withdraw_money(20000)
print()
acc.print_balance()
print()
acc.print_info()


# C:\Users\Dmitry\Scripts\Python\venv\Scripts\python.exe C:/Users/Dmitry/Scripts/Python/DZ_Accaunt_2.py
# Счёт #12345 принадлежит Долгих был открыт.
# **************************************************
# Инф о счёте
# --------------------
# #12345
# Владелец Долгих
# Текущий баланс 1000 RUB
# Проценты: 3%
# --------------------
# #56789 > Новый номер счёта присвоен
# Новый владелец счёта объявлен: Ботвинник
# 0.05 > Процентная ставка установлена
# 100000 > Текущий баланс объявлен
#
# Инф о счёте
# --------------------
# #56789
# Владелец Ботвинник
# Текущий баланс 100000 RUB
# Проценты: 5%
# --------------------
# Состояние счёта в USD: 1300.0 USD
# Состояние счёта в EUR: 1100.0 EUR
#
# Состояние счёта в USD: 200000 USD
#
# Состояние счёта в EUR: 300000 EUR
#
# Текущий баланс 105000.0 RUB
# 3000 RUB было успешно снято
# Текущий баланс 102000.0 RUB
#
# Текущий баланс 102000.0 RUB
#
# 5000 RUB было добавлено
#
# Текущий баланс 107000.0 RUB
#
# 20000 RUB было успешно снято
# Текущий баланс 87000.0 RUB
#
# Текущий баланс 87000.0 RUB
#
# Инф о счёте
# --------------------
# #56789
# Владелец Ботвинник
# Текущий баланс 87000.0 RUB
# Проценты: 5%
# --------------------
# **************************************************
# Счёт #56789 был закрыт.
#
# Process finished with exit code 0
