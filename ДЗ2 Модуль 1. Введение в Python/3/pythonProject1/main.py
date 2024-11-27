# Задание 3
# Пользователь вводит с клавиатуры количество метров. Требуется вывести результат перевода метров в сантиметры, дециметры, миллиметры, мили.

def convert_meters(meters):
    centimeters = meters * 100
    decimeters = meters * 10
    millimeters = meters * 1000
    miles = meters / 1609.344

    return {
        'centimeters': round(centimeters, 2),
        'decimeters': round(decimeters, 2),
        'millimeters': round(millimeters, 2),
        'miles': round(miles, 8)
    }

# Получаем ввод от пользователя
meters_input = float(input("Введите количество метров: "))

# Выполняем конвертацию
results = convert_meters(meters_input)

# Выводим результаты
print(f"{meters_input} метров:")
print(f"\tЦентиметров: {results['centimeters']}")
print(f"\tДециметров: {results['decimeters']}")
print(f"\tМиллиметров: {results['millimeters']}")
print(f"\tМили: {results['miles']}")

