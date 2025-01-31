# Задание 3
# Есть некоторый текст. Посчитайте в этом тексте количество предложений
# и выведите на экран полученный результат.

def count_sentences(text):
    # Подсчет количества предложений
    sentences_count = text.count('.') + text.count('!') + text.count('?')

    # Убираем лишние символы конца предложения, такие как точки после сокращений
    sentences_count -= text.count('...') * 2

    return sentences_count


# Ввод текста пользователем
input_text = input("Введите текст: ")

# Подсчёт предложений
sentences = count_sentences(input_text)

# Вывод результата
print('В вашем тексте', sentences, 'предложений.')
