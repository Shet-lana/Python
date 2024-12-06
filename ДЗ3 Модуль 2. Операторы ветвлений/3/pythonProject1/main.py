# Задание 3
# Пользователь вводит с клавиатуры количество метров. В зависимости от выбора пользователя программа
# переводит метры в мили, дюймы или ярды.

def convert_meters(meters, unit):
    if unit == 'мили':
        return meters * 0.000621371
    elif unit == 'дюймы':
        return meters * 39.3701
    elif unit == 'ярды':
        return meters * 1.09361
    else:
        return None

meters = float(input("Введите количество метров: "))
unit = input("В какой единице измерения перевести? (мили/дюймы/ярды): ").lower()

result = convert_meters(meters, unit)

if result is not None:
    print(f"{meters} метра(ов) равно {result} {unit}.")
else:
    print("Неправильный выбор единицы измерения.")

