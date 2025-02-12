# Панель администрирования библиотеки(обязательно)
# 	Напишите панель администрирования библиотеки.
# 	Обязательные функции(общение через меню) - это добавление книги; удаление книги;
# 	поиск книг по автору, названию, жанру; просмотр добавленных книг

books = []

while True:
    print("Меню:")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Поиск книг по автору")
    print("4. Поиск книг по названию")
    print("5. Поиск книг по жанру")
    print("6. Просмотреть список всех книг")
    print("0. Выход")

    choice = input("Введите номер пункта меню: ")

    if choice == '1':
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        genre = input("Введите жанр книги: ")

        books.append({'title': title, 'author': author, 'genre': genre})

        print("Книга", title, "успешно добавлена.")

    elif choice == '2':
        book_to_delete = input("Введите название книги, которую хотите удалить: ")

        for i in range(len(books)):
            if books[i]['title'] == book_to_delete:
                del books[i]
                break

        else:
            print("Книги с названием", book_to_delete, "нет в библиотеке.")

    elif choice == '3':
        search_author = input("Введите имя автора для поиска: ")

        found_books = [book for book in books if book['author'].lower() == search_author.lower()]

        if found_books:
            for book in found_books:
                print(book['title'] + " (" + book['author'] + ", " + book['genre'] + ")")
        else:
            print("Книг автора", search_author, "не найдено.")

    elif choice == '4':
        search_title = input("Введите название книги для поиска: ")

        found_books = [book for book in books if book['title'].lower() == search_title.lower()]

        if found_books:
            for book in found_books:
                print(book['title'] + " (" + book['author'] + ", " + book['genre'] + ")")
        else:
            print("Книгу с названием", search_title, "не найдено.")

    elif choice == '5':
        search_genre = input("Введите жанр для поиска: ")

        found_books = [book for book in books if book['genre'].lower() == search_genre.lower()]

        if found_books:
            for book in found_books:
                print(book['title'] + " (" + book['author'] + ", " + book['genre'] + ")")
        else:
            print("Книг жанра", search_genre, "не найдено.")

    elif choice == '6':
        if books:
            for book in books:
                print(book['title'] + " (" + book['author'] + ", " + book['genre'] + ")")
        else:
            print("Библиотека пуста.")

    elif choice == '0':
        print("Выход из программы.")
        break

    else:
        print("Неверный ввод. Попробуйте еще раз.")
