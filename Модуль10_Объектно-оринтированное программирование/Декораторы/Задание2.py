# Добавьте к первому заданию возможность передавать
# границы диапазона для поиска всех простых чисел.

import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'\nВычисление заняло {execution_time:.6f} секунд.\n')
        return result

    return wrapper


@timer_decorator
def find_primes_in_range(start, end):
    primes = []
    for num in range(max(2, start), end + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


if __name__ == "__main__":
    try:
        start_number = int(input('Введите начальное число диапазона: '))
        end_number = int(input('Введите конечное число диапазона: '))

        # Проверяем корректность введённых значений
        if start_number > end_number or start_number <= 0 or end_number <= 0:
            raise ValueError(
                'Диапазон некорректен! Начальное значение должно быть меньше конечного и оба значения больше нуля.')

        # Получаем простые числа в указанном диапазоне
        primes_between = find_primes_in_range(start_number, end_number)
        print(f'Простые числа между {start_number} и {end_number}:\n{primes_between}')
    except ValueError as e:
        print(e)