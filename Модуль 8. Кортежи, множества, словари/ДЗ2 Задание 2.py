# Создайте программу «Англо-французский словарь».
# Нужно хранить слово на английском языке и его перевод на французский.
# Требуется реализовать возможность добавления, удаления, поиска, замены данных.
# Используйте словарь для хранения информации.

def add_word(dictionary):
    """Добавление нового слова в словарь"""
    english_word = input('Введите английское слово: ').strip()
    french_translation = input('Введите перевод на французский: ').strip()

    if english_word in dictionary:
        print(f'Слово {english_word} уже существует в словаре.')
    else:
        dictionary[english_word] = french_translation
        print(f'Слово {english_word} успешно добавлено в словарь.')


def delete_word(dictionary):
    """Удаление слова из словаря"""
    english_word = input('Введите английское слово для удаления: ').strip()

    if english_word in dictionary:
        del dictionary[english_word]
        print(f'Слово {english_word} удалено из словаря.')
    else:
        print(f'Слова {english_word} нет в словаре.')


def search_word(dictionary):
    """Поиск перевода слова"""
    english_word = input('Введите английское слово для поиска: ').strip()

    if english_word in dictionary:
        print(f'Перевод слова {english_word} на французский: {dictionary[english_word]}')
    else:
        print(f'Слова {english_word} нет в словаре.')


def replace_word(dictionary):
    """Замена перевода слова"""
    english_word = input('Введите английское слово для замены: ').strip()

    if english_word in dictionary:
        new_french_translation = input('Введите новый перевод на французский: ').strip()
        dictionary[english_word] = new_french_translation
        print(f'Перевод слова {english_word} успешно заменён на {new_french_translation}.')
    else:
        print(f'Слова {english_word} нет в словаре.')


# Словарь для хранения английских слов и их французских переводов
dictionary = {}

while True:
    print('Меню:')
    print('1. Добавить слово')
    print('2. Удалить слово')
    print('3. Найти перевод')
    print('4. Заменить перевод')
    print('0. Выход')

    choice = input('Ваш выбор: ')

    if choice == '1':
        add_word(dictionary)
    elif choice == '2':
        delete_word(dictionary)
    elif choice == '3':
        search_word(dictionary)
    elif choice == '4':
        replace_word(dictionary)
    elif choice == '0':
        break
    else:
        print('Неверный ввод. Попробуйте снова.')
