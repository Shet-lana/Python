# Задание 2
# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
# на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел.

# три числа от пользователя
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

# Запрашиваем у пользователя, какую операцию он хочет выполнить
choice = input("Выберите операцию:\n1. Максимум\n2. Минимум\n3. Среднее арифметическое\nВаш выбор: ")

if choice == '1':
    # Находим максимум из трех чисел
    result = max(a, b, c)
elif choice == '2':
    # Находим минимум из трех чисел
    result = min(a, b, c)
elif choice == '3':
    # Вычисляем среднее арифметическое трех чисел
    result = (a + b + c) / 3


print(f'Результат: {result}')