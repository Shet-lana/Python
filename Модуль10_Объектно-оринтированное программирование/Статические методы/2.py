# Задание 2
# Создайте класс для конвертирования температуры из Цельсия в Фаренгейт и наоборот.
# У класса должно быть два статических метода: для перевода из Цельсия в Фаренгейт
# и для перевода из Фаренгейта в Цельсий. Также класс должен считать количество
# подсчетов температуры и возвращать это значение с помощью статического метода

class TemperatureConverter:
    conversions = 0  # Количество выполнений конверсий

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 9/5) + 32
        TemperatureConverter.conversions += 1
        return fahrenheit

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        TemperatureConverter.conversions += 1
        return celsius

    @staticmethod
    def get_conversions_count():
        return TemperatureConverter.conversions


temp1 = TemperatureConverter.celsius_to_fahrenheit(30)
temp2 = TemperatureConverter.fahrenheit_to_celsius(86)
print(TemperatureConverter.get_conversions_count())
