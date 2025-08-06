class Logger:
    _instance = None

    def __new__(cls, output_type='console'):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.output_type = output_type
        return cls._instance

    def log(self, message):
        if self.output_type == 'console':
            print(message)
        elif self.output_type == 'file':
            with open('log.txt', 'a') as file:
                file.write(message + '\n')


# Основная программа
def main():
    logger = Logger(output_type='file')  # Логируем в файл

    try:
        numbers_input = input('Введите список чисел через пробел: ')
        path_to_file = input('Укажите путь к файлу для сохранения результатов: ')

        # Преобразуем введённые строки в числа
        numbers = list(map(float, numbers_input.split()))

        # Определяем минимальное и максимальное значение
        min_value = min(numbers)
        max_value = max(numbers)

        # Запись чисел и результата в указанный файл
        with open(path_to_file, 'w') as f:
            for num in numbers:
                f.write(f'{num}\n')
            f.write(f'\nМинимальное число: {min_value}\nМаксимальное число: {max_value}')

        # Логируем операции
        logger.log(f'Введены числа: {numbers_input}')
        logger.log(f'Сохранено в файл: {path_to_file}')
        logger.log(f'Минимальное число: {min_value}, Максимальное число: {max_value}')

        # Выводим результаты на экран
        print('\nОтображаем введённые числа:')
        for num in numbers:
            print(num)
        print(f'\nМинимальное число: {min_value}')
        print(f'Максимальное число: {max_value}')

    except Exception as e:
        logger.log(f'Произошла ошибка: {str(e)}')
        print('Ошибка обработки ввода.')


if __name__ == "__main__":
    main()