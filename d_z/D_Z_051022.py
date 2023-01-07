class Book:
    name = "name"
    year = "0000"
    publisher = "publisher"
    genre = "genre"
    author = "author"
    price = "000000"

    def print_info(self):
        print(" Данные книги ".center(40, "*"))
        print(f"Название книги: {self.name}\nГод выпуска: {self.year}\n"
              f"Издатель: {self.publisher}\nЖанр: {self.genre}\n"
              f"Автор: {self.author}\nЦена: {self.price}")
        print("=" * 40)

    def input_info(self, name, year, publisher, genre, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def set_name(self, n):       # Ввести/поменять название книги
        self.name = n

    def get_name(self):          # Вывести название книги
        return self.name

    def set_year(self, y):       # Поменять год издания
        self.year = y

    def get_year(self):
        return self.year

    def set_publisher(self, p):  # Ввод/смена издателя
        self.publisher = p

    def get_publisher(self):
        return self.publisher

    def set_genre(self, g):      # Ввод/смена жанра
        self.genre = g

    def get_genre(self):
        return self.genre

    def set_author(self, a):     # Ввод/смена автора
        self.author = a

    def get_author(self):
        return self.author

    def set_price(self, pr):     # Ввод/смена цены
        self.price = pr

    def get_price(self):
        return self.price

b1 = Book()
b1.print_info()
b1.input_info("Романовы", "2006", "Белый город", "История", "Божерянов И.Н.", "10000")
b1.print_info()
b1.set_name("Моя система")
print(b1.get_name())
b1.set_year("1974")
print(b1.get_year())
b1.set_publisher("Физкультура и спорт")
print(b1.get_publisher())
b1.set_author("А. Нимцович")
print(b1.get_author())
b1.set_price("1р 06к")
print(b1.get_price())


    