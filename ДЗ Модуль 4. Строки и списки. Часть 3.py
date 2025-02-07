# Два списка целых заполняются случайными числами.
# Необходимо:
# ■ Сформировать третий список, содержащий элементы
# обоих списков;
# ■ Сформировать третий список, содержащий элементы
# обоих списков без повторений;
# ■ Сформировать третий список, содержащий элементы
# общие для двух списков;
# ■ Сформировать третий список, содержащий только
# уникальные элементы каждого из списков;
# ■ Сформировать третий список, содержащий только
# минимальное и максимальное значение каждого и

import random

# Генерация двух списков случайных чисел
list_1 = [random.randint(0, 10) for _ in range(10)]
list_2 = [random.randint(0, 10) for _ in range(10)]

print("Список 1:", list_1)
print("Список 2:", list_2)

# Объединение элементов обоих списков
combined_list = list_1 + list_2
print("Объединенный список:", combined_list)

# Объединение элементов без повторений
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

unique_combined_list = remove_duplicates(combined_list)
print("Объединенный список без повторений:", unique_combined_list)

# Общие элементы двух списков
common_elements = []
for element in list_1:
    if element in list_2:
        common_elements.append(element)

print("Общие элементы:", common_elements)

# Уникальные элементы каждого из списков
unique_elements = []
for element in list_1:
    if element not in list_2:
        unique_elements.append(element)
for element in list_2:
    if element not in list_1:
        unique_elements.append(element)

print("Уникальные элементы:", unique_elements)

# Минимум и максимум каждого списка
min_max_values = [min(list_1), max(list_1), min(list_2), max(list_2)]
print("Минимум и максимум каждого списка:", min_max_values)
