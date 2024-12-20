# Задание 1
# Пользователь вводит с клавиатурыдва числа. Нужно
# посчитать отдельно сумму четных, нечетных и чисел,
# кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы.

# Запрашиваем у пользователя начало и конец диапазона
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

# Инициализация переменных для сумм и счетчиков
even_sum = 0
odd_sum = 0
multiple_of_nine_sum = 0

even_count = 0
odd_count = 0
multiple_of_nine_count = 0

# Проход по всем числам в диапазоне
for number in range(start, end + 1):
    # Проверка на четность
    if number % 2 == 0:
        even_sum += number
        even_count += 1
    else:
        odd_sum += number
        odd_count += 1

    # Проверка на кратность 9
    if number % 9 == 0:
        multiple_of_nine_sum += number
        multiple_of_nine_count += 1

# Вычисление средних значений
if even_count != 0:
    even_avg = even_sum / even_count
else:
    even_avg = 0

if odd_count != 0:
    odd_avg = odd_sum / odd_count
else:
    odd_avg = 0

if multiple_of_nine_count != 0:
    multiple_of_nine_avg = multiple_of_nine_sum / multiple_of_nine_count
else:
    multiple_of_nine_avg = 0

# Вывод результатов
print(f"Сумма чётных чисел: {even_sum}, среднее арифметическое: {even_avg:.2f}")
print(f"Сумма нечётных чисел: {odd_sum}, среднее арифметическое: {odd_avg:.2f}")
print(f"Сумма чисел, кратных 9: {multiple_of_nine_sum}, среднее арифметическое: {multiple_of_nine_avg:.2f}")
