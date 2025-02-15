
# Задание 1
# Напишите функцию, которая отображает на экран
# форматированный текст, указанный ниже:
# “Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself.”
# Bill Gates

def bill_gates_quote():
    quote = (
        '"Don’t compare yourself with anyone in this world…\n'
        'if you do so, you are insulting yourself."\n'
        '\t\t\t\t\t\t\t\tBill Gates'
    )
    print(quote)

bill_gates_quote()

# -------------------------------------------
# Задание 2
# Напишите функцию, которая принимает два числа
# в качестве параметра и отображает все четные числа между ними.

def task_2(num1, num2):
    start = min(num1, num2)
    final = max(num1, num2)

    for i in range(start, final + 1):
        if i % 2 == 0:
            print(i, end=' ')
    print()


task_2(4, 18)

# -------------------------------------------
# Задание 3
# Напишите функцию, которая отображает пустой или
# заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны квадрата,
# символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный;
# ■ если False, квадрат пустой.

def draw_square(size: int, char: str, is_filled: bool) -> None:
    """
    Отображает пустой или заполненный квадрат из заданного символа.

    :param size: Длина стороны квадрата.
    :param char: Символ, которым заполняется квадрат.
    :param is_filled: Логический флаг, определяющий, должен ли квадрат быть заполненным.
    """
    for i in range(size):
        if is_filled or i == 0 or i == (size - 1) :  # Верхняя и нижняя границы всегда печатаются полностью
            print(char * size)
        else:  # Печатаем боковые границы пустого квадрата
            print(char + ' ' * (size - 2) + char)

draw_square(4, '*', False)

# -------------------------------------------
# Задание 4
# Напишите функцию, которая возвращает минимальное
# из пяти чисел. Числа передаются в качестве параметров.

def smallest_of_five(num1, num2, num3, num4, num5):
    return min(num1, num2, num3, num4, num5)

a = smallest_of_five(1, 2, -3, 4, 5)
print(a)

# -------------------------------------------
# Задание 5
# Напишите функцию, которая возвращает произведение чисел в указанном диапазоне.
# Границы диапазона передаются в качестве параметров. Если границы диапазона
# перепутаны (например, 5 — верхняя граница, 25 — нижняя граница),
# их нужно поменять местами.

def multiplication_result(start_range, end_range):
    # Меняем границы местами, если перепутали
    if start_range > end_range:
        start_range, end_range = end_range, start_range

    # Переменная для хранения произведения
    product = 1

    # Проходим по всем числам в диапазоне включительно
    for number in range(start_range, end_range + 1):
        product *= number

    return product

result = multiplication_result(2, 4)
print(result)

# -------------------------------------------
# Задание 6
# Напишите функцию, которая считает количество цифр в числе.
# Число передаётся в качестве параметра. Из функции нужно вернуть
# полученное количество цифр. Например, если передали 3456, количество цифр будет 4.

def count_digits(number):
    # Преобразуем число в строку, берем модуль (чтобы убрать знак минус),
    # удаляем десятичную точку и считаем длину оставшейся строки
    return len(str(abs(number)).replace('.', ''))

a = count_digits(-34.501)
b = count_digits(12345)
c = count_digits(0.0001)
d = count_digits(-100)

print(a)
print(b)
print(c)
print(d)

# -------------------------------------------
# Задание 7
# Напишите функцию, которая проверяет является ли число палиндромом.
# Число передаётся в качестве параметра. Если число палиндром нужно вернуть из функции
# true, иначе false. «Палиндром» — это число, у которого первая часть цифр равна
# второй перевернутой части цифр. Например, 123321 — палиндром (первая часть 123, вторая 321, которая
# после переворота становится 123), 546645 — палиндром, а 421987 — не палиндром.

def is_palindrome(number):
    # Проверяем, является ли число целым
    if not isinstance(number, int):
        return False

    # Преобразуем число в строку и сравниваем с перевёрнутой строкой
    string_representation = str(number)
    reversed_string = string_representation[::-1]
    return string_representation == reversed_string

print(is_palindrome(123321))
print(is_palindrome(546645))
print(is_palindrome(421987))
print(is_palindrome(10.01))
print(is_palindrome("123"))


