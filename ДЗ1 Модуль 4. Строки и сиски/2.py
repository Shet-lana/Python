# Задание 2
# Пользователь вводит с клавиатуры некоторый текст,
# после чегопользователь вводит список зарезервированных
# слов. Необходимо найти в тексте все зарезервированные
# слова и изменить их регистр на верхний. Вывести на экран измененный текст

def replace_reserved_words(text, reserved_words):
    # Преобразуем текст в нижний регистр, чтобы избежать проблем с регистрами при поиске
    text_lower = text.lower()

    for word in reserved_words:
        # Находим индекс каждого зарезервированного слова в нижнем регистре текста
        index = text_lower.find(word)

        if index != -1:
            # Если слово найдено, заменяем его в исходном тексте на заглавный регистр
            text = text[:index] + word.upper() + text[index + len(word):]

    return text


# Вводим текст от пользователя
input_text = input("Введите текст: ")

# Вводим список зарезервированных слов
reserved_words = input("Введите список зарезервированных слов через пробел: ").split()

# Вызываем функцию замены зарезервированных слов
result_text = replace_reserved_words(input_text, reserved_words)

# Выводим результат
print(result_text)
