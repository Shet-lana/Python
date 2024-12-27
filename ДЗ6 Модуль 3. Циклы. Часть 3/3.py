# Задание 3
# Подсчитать количество целых чисел в диапазоне от
# 100 до 9999 у которых все цифры разные.

count = 0

for num in range(100, 10000):
    digits = set()

    for digit in str(num):
        if digit in digits:
            break
        else:
            digits.add(digit)
    else:
        count += 1

print(count)
