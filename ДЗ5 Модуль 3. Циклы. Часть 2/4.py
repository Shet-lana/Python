# Задание 4
# Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму,
# максимум и минимум, введенных чисел. Когда пользователь вводит число 7
# программа прекращает свою работу и выводит на экран надпись «Good bye!»

total_sum = 0
max_number = None
min_number = None

while True:
    number = float(input("Введите число: "))

    if number == 7:
        print("Good bye!")
        break

    total_sum += number

    if max_number is None or number > max_number:
        max_number = number

    if min_number is None or number < min_number:
        min_number = number

print(f"Сумма введённых чисел: {total_sum}")
print(f"Максимальное число: {max_number}")
print(f"Минимальное число: {min_number}")
