# Задание 3
# Пользователь вводит с клавиатурычисла. Если число
# больше нуля нужно вывести надпись «Numberis positive»,
# если меньше нуля «Numberis negative», если равно нулю
# «Number is equal to zero». Когда пользователь вводит число 7
# программа прекращает свою работу и выводит
# на экран надпись «Good bye!»

while True:
    number = float(input("Введите число: "))

    if number > 0:
        print("Number is positive")
    elif number < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")

    if number == 7:
        print("Good bye!")
        break
