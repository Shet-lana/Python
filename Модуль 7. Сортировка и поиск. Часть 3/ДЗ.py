# Задание 1
# Есть четыре списка целых. Необходимо их объединить
# в пятом списке. Полученный результат в зависимости от
# выбора пользователя отсортировать по убыванию или
# возрастанию. Найти значение, введенное пользователем,
# с использованием линейного поиска.

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

# Вводим списки
list1 = [10, 20, 30]
list2 = [40, 50, 60]
list3 = [70, 80, 90]
list4 = [100, 110, 120]

# Объединяем списки
combined_list = list1 + list2 + list3 + list4

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
print("Отсортированный список:", combined_list)

# Запрашиваем значение для поиска
target = int(input("Введите число для поиска: "))

# Выполняем линейный поиск
index = linear_search(combined_list, target)

if index != -1:
    print(f"Значение {target} найдено на позиции {index}.")
else:
    print(f"Значение {target} не найдено.")