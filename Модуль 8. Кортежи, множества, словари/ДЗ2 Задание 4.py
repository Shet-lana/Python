# Создайте программу «Книжная коллекция». Нужно хранить информацию о книгах:
# автор, название книги, жанр, год выпуска, количество страниц, издательство.
# Требуется реализовать возможность добавления, удаления, поиска, замены данных.
# Используйте словарь для хранения информации.

# Словарь для хранения коллекции книг
books_collection = {}


def add_book():
    isbn = input('Введите ISBN книги: ')
    if isbn in books_collection:
        print(f'Книга с ISBN {isbn} уже существует.')
        return

    author = input('Введите автора книги: ')
    title = input('Введите название книги: ')
    genre = input('Введите жанр книги: ')
    year = int(input('Введите год выпуска книги: '))
    pages = int(input('Введите количество страниц: '))
    publisher = input('Введите издательство: ')

    book_data = (author, title, genre, year, pages, publisher)
    books_collection[isbn] = book_data
    print(f'Книга успешно добавлена!')


def remove_book():
    isbn = input('Введите ISBN книги, которую хотите удалить: ')
    if isbn not in books_collection:
        print(f'Книги с ISBN {isbn} не найдено.')
        return

    del books_collection[isbn]
    print(f'Книга удалена.')


def search_book():
    isbn = input('Введите ISBN книги, которую хотите найти: ')
    if isbn not in books_collection:
        print(f'Книги с ISBN {isbn} не найдено.')
        return

    book_data = books_collection[isbn]
    print(f'Автор: {book_data[0]}')
    print(f'Название: {book_data[1]}')
    print(f'Жанр: {book_data[2]}')
    print(f'Год выпуска: {book_data[3]}')
    print(f'Количество страниц: {book_data[4]}')
    print(f'Издательство: {book_data[5]}')


def replace_book():
    isbn = input('Введите ISBN книги, данные которой хотите заменить: ')
    if isbn not in books_collection:
        print(f'Книги с ISBN {isbn} не найдено.')
        return

    author = input('Введите нового автора книги: ')
    title = input('Введите новое название книги: ')
    genre = input('Введите новый жанр книги: ')
    year = int(input('Введите новый год выпуска книги: '))
    pages = int(input('Введите новое количество страниц: '))
    publisher = input('Введите новое издательство: ')

    new_book_data = (author, title, genre, year, pages, publisher)
    books_collection[isbn] = new_book_data
    print(f'Данные книги успешно заменены!')


while True:
    print('Меню:')
    print('1. Добавить книгу')
    print('2. Удалить книгу')
    print('3. Найти книгу')
    print('4. Заменить данные книги')
    print('5. Выход')

    choice = input('Ваш выбор: ')

    if choice == '1':
        add_book()
    elif choice == '2':
        remove_book()
    elif choice == '3':
        search_book()
    elif choice == '4':
        replace_book()
    elif choice == '5':
        break
    else:
        print('Неверный ввод. Попробуйте снова.')