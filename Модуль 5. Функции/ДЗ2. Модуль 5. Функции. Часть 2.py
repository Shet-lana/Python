# Задание 1
# Напишите функцию, вычисляющую произведение элементов
# списка целых. Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.


def multiplication_elements(list_of_integers):
    m = 1
    for element in list_of_integers:
        m = m * element
    return m

list_of_integers = [1, 2, 3, 4]
result = multiplication_elements(list_of_integers)
print(result)


# ----------------------------------------------------
# Задание 2
# Напишите функцию для нахождения минимума в
# списке целых. Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.

def smallest_element(list_of_integers):
    s = list_of_integers[0]  # Инициализируем переменную минимального значения первым элементом списка
    for element in list_of_integers:
        if s > element:      # Если текущий элемент меньше текущего минимума, обновляем минимум
            s = element
    return s                # Возвращаем найденный минимум

a = smallest_element([2, 5, 3, 1, -11, 87, 9, -2])
print(a)

# ----------------------------------------------------
# Задание 3
# Напишите функцию, определяющую количество простых
# чисел в списке целых. Список передаётся в качестве
# параметра. Полученный результат возвращается из функции.

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.sqrt(n)) + 1  # Определяет верхнюю границу для проверки делителей. Квадратный корень из числа плюс единица дает максимально возможное значение делителя, который еще может быть у числа n.
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

def number_of_primes(list_of_integers):
    number_of_primes = 0
    for element in list_of_integers:
        if is_prime(element):    # Вызывает функцию is_prime для проверки, является ли текущее число простым.
            number_of_primes += 1
    return number_of_primes

a = number_of_primes([2, 5, 4, -11, 137, -2, 2, 1, 0, 3])
print(a)  # 5


# ----------------------------------------------------
# Задание 4
# Напишите функцию, удаляющую из списка целых
# некоторое заданное число. Из функции нужно вернуть
# количество удаленных элементов.

def remove_integer_from_list(integer, lst):
    new_lst = [item for item in lst if item != integer]
    removed_count = len(lst) - len(new_lst)
    return removed_count, new_lst

a_list = [2, 5, 4, 2, 3, -2, 2, 1, 0, 3]
a_integer = 2

count, result_list = remove_integer_from_list(a_integer, a_list)
print(count)
print(result_list)

# ----------------------------------------------------
# Задание 5
# Напишите функцию, которая получает два списка в
# качестве параметра и возвращает список, содержащий
# элементы обоих списков.

def concatenate_two_lists(list1, list2):
    return list1 + list2


a_list = [2, 5, 4, 3]
b_list = [12, 15, 14, 13]
c = concatenate_two_lists(a_list, b_list)
print(c)


# ----------------------------------------------------
# Задание 6
# Напишите функцию, высчитывающую степень каждого
# элемента списка целых. Значение для степени передаётся
# в качестве параметра, список тоже передаётся в качестве
# параметра. Функция возвращает новый список, содержащий
# полученные результаты.

def power_of_elements_list(power, list_of_integers):
    powered_list = []
    for element in list_of_integers:
        powered_list.append(element ** power)
    return powered_list

a_power = 4
a_list = [2, 5, 4, 3, -2, 1, 0, 3]
p = power_of_elements_list(a_power, a_list)
print(p)  # [16, 625, 256, 81, 16, 1, 0, 81]

