# Задание 1
# К уже реализованному классу «Дробь» добавьте статический метод,
# который при вызове возвращает количество созданных объектов класса «Дробь».

class Fraction:
    count = 0  # Количество созданных дробей

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.count += 1  # Увеличение количества при создании новой дроби

    @staticmethod
    def get_count():
        return Fraction.count


frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)
print(Fraction.get_count())
