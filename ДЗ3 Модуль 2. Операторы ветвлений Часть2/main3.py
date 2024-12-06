# Задание 3
# Пользователь вводит с клавиатуры число. Если число
# больше нуля нужно вывести надпись «Numberis positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero»

# Запрашиваем у пользователя ввод числа
number = float(input("Введите число: "))

# Проверяем знак числа
if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is equal to zero")
