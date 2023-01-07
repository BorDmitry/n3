            # 1-й вариант задачи "АККАУНТ"
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

    def get_num(self):
        return self.__num

    def set_num(self, n):
        self.__num = n

    def get_surname(self):
        return self.__surname

    def set_surname(self, s):
        self.__surname = s

    def get_percent(self):
        return self.__percent

    def set_percent(self, p):
        self.__percent = p

    def get_value(self):
        return self.__value

    def set_value(self, v):
        self.__value = v

    def __del__(self):
        print('*' * 50)
        print(f'Счёт #{self.__num} был закрыт.')

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
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f'Состояние счёта долларах: {usd_val} {Account.suffix2}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f'Состояние счёта в евро: {eur_val} {Account.suffix1}')

    def print_balance(self):
        print(f'Текущий баланс {self.__value} {Account.suffix}')

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
        print('Проценты начислены')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f'К сожалению Вы не можете снять {val} RUB')
        else:
            self.__value -= val
            print(f'{val} RUB было успешно снято')
            self.print_balance()
    def add_money(self, val):

        self.__value += val
        print(f'{val} RUB было добавлено')


acc = Account('12345', 'Долгих', 0.03, 1000)
acc.print_info()

acc.set_num(16789)
print(acc.get_num())

acc.set_surname('Алехин')
print(acc.get_surname())

acc.set_percent(0.04)
print(acc.get_percent())

acc.set_value(2000)
print(acc.get_value())

acc.print_info()
# print(acc.__dict__)

acc.convert_to_usd()
acc.convert_to_eur()

Account.set_eur_rate(3)
acc.convert_to_eur()

Account.set_usd_rate(5)
acc.convert_to_usd()

acc.add_percents()

acc.withdraw_money(3000)

acc.add_money(5000)

acc.withdraw_money(3000)

acc.withdraw_money(1000)

# Вывод в консоле:

# C:\Users\Dmitry\Scripts\Python\venv\Scripts\python.exe C:/Users/Dmitry/Scripts/Python/DZ_account.py
# Счёт #12345 принадлежит Долгих был открыт.
# **************************************************
# Инф о счёте
# --------------------
# #12345
# Владелец Долгих
# Текущий баланс 1000 RUB
# Проценты: 3%
# --------------------
# 16789
# Алехин
# 0.04
# 2000
# Инф о счёте
# --------------------
# #16789
# Владелец Алехин
# Текущий баланс 2000 RUB
# Проценты: 4%
# --------------------
# Состояние счёта долларах: 26.0 USD
# Состояние счёта в евро: 22.0 EUR
# Состояние счёта в евро: 6000 EUR
# Состояние счёта долларах: 10000 USD
# Проценты начислены
# Текущий баланс 2080.0 RUB
# К сожалению Вы не можете снять 3000 RUB
# 5000 RUB было добавлено
# 3000 RUB было успешно снято
# Текущий баланс 4080.0 RUB
# 1000 RUB было успешно снято
# Текущий баланс 3080.0 RUB
# **************************************************
# Счёт #16789 был закрыт.
#
# Process finished with exit code 0


