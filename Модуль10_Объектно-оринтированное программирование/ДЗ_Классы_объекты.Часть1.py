# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя, объем двигателя,
# цвет машины, цену. Реализуйте методы класса для ввода данных, вывода данных,
# реализуйте доступ к отдельным полям через методы класса


class Car:
    def __init__(self):
        self.model_name = None  # Название модели
        self.year = None  # Год выпуска
        self.manufacturer = None  # Производитель
        self.engine_volume = None  # Объем двигателя
        self.color = None  # Цвет авто
        self.price = None  # Цена

    # Метод для ввода всех данных сразу
    def input_data(self):
        print("Введите характеристики автомобиля:")
        self.model_name = input("Название модели: ")
        self.year = int(input("Год выпуска: "))
        self.manufacturer = input("Производитель: ")
        self.engine_volume = float(input("Объем двигателя (литры): "))
        self.color = input("Цвет автомобиля: ")
        self.price = float(input("Цена ($): "))

    # Метод для вывода всех данных
    def output_data(self):
        print(f"\nХарактеристики автомобиля:\n"
              f"Модель: {self.model_name}\n"
              f"Год выпуска: {self.year}\n"
              f"Производитель: {self.manufacturer}\n"
              f"Объем двигателя: {self.engine_volume:.1f} л\n"
              f"Цвет: {self.color}\n"
              f"Цена: ${self.price:.2f}")

    # Методы для доступа к отдельным полям
    def set_model_name(self, model_name):
        self.model_name = model_name

    def get_model_name(self):
        return self.model_name

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        return self.manufacturer

    def set_engine_volume(self, engine_volume):
        self.engine_volume = engine_volume

    def get_engine_volume(self):
        return self.engine_volume

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


# Тестируем класс
car = Car()
car.input_data()
car.output_data()
print("\nДоступ к отдельным полям:")
print(car.get_model_name())
print(car.get_year())

# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в  полях класса: название книги,
# год выпуска, издателя, жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

class Book:
    def __init__(self):
        self.title = None  # Название книги
        self.year = None  # Год издания
        self.publisher = None  # Издатель
        self.genre = None  # Жанр
        self.author = None  # Автор
        self.price = None  # Цена

    # Метод для ввода всех данных сразу
    def input_data(self):
        print("Введите данные о книге:")
        self.title = input("Название книги: ")
        self.year = int(input("Год издания: "))
        self.publisher = input("Издательство: ")
        self.genre = input("Жанр: ")
        self.author = input("Автор: ")
        self.price = float(input("Цена ($): "))

    # Метод для вывода всех данных
    def output_data(self):
        print(f"\nДанные о книге:\n"
              f"Название: {self.title}\n"
              f"Год издания: {self.year}\n"
              f"Издательство: {self.publisher}\n"
              f"Жанр: {self.genre}\n"
              f"Автор: {self.author}\n"
              f"Цена: ${self.price:.2f}")

    # Методы для доступа к отдельным полям
    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_publisher(self):
        return self.publisher

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


# Тестируем класс
book = Book()
book.input_data()
book.output_data()
print("\nДоступ к отдельным полям:")
print(book.get_title())
print(book.get_year())

# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона,
# дату открытия, страну, город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.


class Stadium:
    def __init__(self):
        self.name = None  # Название стадиона
        self.open_date = None  # Дата открытия
        self.country = None  # Страна расположения
        self.city = None  # Город расположения
        self.capacity = None  # Вместимость зрителей

    # Метод для ввода всех данных сразу
    def input_data(self):
        print("Введите данные о стадионе:")
        self.name = input("Название стадиона: ")
        self.open_date = input("Дата открытия (ДД.ММ.ГГГГ): ")
        self.country = input("Страна: ")
        self.city = input("Город: ")
        self.capacity = int(input("Вместимость (количество мест): "))

    # Метод для вывода всех данных
    def output_data(self):
        print(f"\nИнформация о стадионе:\n"
              f"Название: {self.name}\n"
              f"Дата открытия: {self.open_date}\n"
              f"Страна: {self.country}\n"
              f"Город: {self.city}\n"
              f"Вместимость: {self.capacity} человек")

    # Методы для доступа к отдельным полям
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_open_date(self, open_date):
        self.open_date = open_date

    def get_open_date(self):
        return self.open_date

    def set_country(self, country):
        self.country = country

    def get_country(self):
        return self.country

    def set_city(self, city):
        self.city = city

    def get_city(self):
        return self.city

    def set_capacity(self, capacity):
        self.capacity = capacity

    def get_capacity(self):
        return self.capacity


# Тестируем класс
stadium = Stadium()
stadium.input_data()
stadium.output_data()
print("\nДоступ к отдельным полям:")
print(stadium.get_name())
print(stadium.get_open_date())
