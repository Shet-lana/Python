# Задание 3
# Создайте класс для перевода из метрической системы в английскую и наоборот.
# Функциональность необходимо реализовать в виде статических методов.
# Обязательно реализуйте перевод мер длины

class UnitConverter:
    @staticmethod
    def meters_to_feet(meters):
        feet = meters * 3.28084
        return feet

    @staticmethod
    def feet_to_meters(feet):
        meters = feet / 3.28084
        return meters


length_in_meters = UnitConverter.feet_to_meters(10)
length_in_feet = UnitConverter.meters_to_feet(5)
print(length_in_meters)  # ~3.048 метров
print(length_in_feet)   # ~16.404 фута
