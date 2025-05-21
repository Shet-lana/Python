# Задание 3
# Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы
# с деньгами. В классе должны быть предусмотрены поле для хранения целой части денег
# (доллары, евро, гривны и т.д.) и поле для хранения копеек (центы, евроценты,
# копейки и т.д.). Реализовать методы для вывода суммы на экран,
# задания значений для частей.

class Money:
    def __init__(self, whole_part=0, fractional_part=0):
        self.whole_part = whole_part
        self.fractional_part = fractional_part

    def display(self):
        print(f"{self.whole_part}.{self.fractional_part:02d}")

    def set_values(self, whole_part, fractional_part):
        self.whole_part = whole_part
        self.fractional_part = fractional_part


# Пример использования
money = Money(10, 99)
money.display()  # Вывод: 10.99

money.set_values(5, 50)
money.display()  # Вывод: 5.50
