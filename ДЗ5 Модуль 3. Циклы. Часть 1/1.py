# Задание 1
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать все
# числа в этом диапазоне по следующему правилу: если
# число кратно 7, его надо выводить на экран.

# Запрашиваем у пользователя начало и конец диапазона
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

# Проходим по всем числам от start до end включительно
for number in range(start, end + 1):
    # Проверяем, делится ли число на 7 без остатка
    if number % 7 == 0:
        print(number)
