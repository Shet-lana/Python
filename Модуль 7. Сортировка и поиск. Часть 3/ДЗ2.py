# Задание 2
# Есть четыре списка целых. Необходимо объединить
# в пятом списке только те элементы, которые уникальны
# для каждого списка. Полученный результат в зависимости
# от выбора пользователя отсортировать по убыванию или
# возрастанию. Найти значение, введенное пользователем,
# с использованием бинарного поиска

from bisect import bisect_left


# Функция для бинарного поиска
def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# Вводим списки
list1 = [10, 20, 30, 40]
list2 = [40, 50, 60, 80]
list3 = [70, 80, 90, 50]
list4 = [100, 110, 120]

# Объединяем уникальные элементы из всех списков
unique_elements = set(list1 + list2 + list3 + list4)
combined_list = list(unique_elements)

# Запрашиваем выбор пользователя
print("Выберите способ сортировки:")
print("1. По возрастанию")
print("2. По убыванию")
choice = int(input("Ваш выбор: "))

if choice == 1:
    # Сортировка по возрастанию
    combined_list.sort()
elif choice == 2:
    # Сортировка по убыванию
    combined_list.sort(reverse=True)
else:
    print("Неверный ввод.")

# Выводим отсортированный список
print("Отсортированный список уникальных элементов:", combined_list)

# Запрашиваем значение для поиска
target = int(input("Введите число для поиска: "))

# Выполняем бинарный поиск
index = binary_search(combined_list, target)

if index != -1:
    print(f"Значение {target} найдено на позиции {index}.")
else:
    print(f"Значение {target} не найдено.")