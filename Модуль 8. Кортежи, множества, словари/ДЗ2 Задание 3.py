# Создайте программу «Фирма». Нужно хранить информацию о человеке:
# ФИО, телефон, рабочий email, название должности, номер кабинета, skype.
# Требуется реализовать возможность добавления, удаления, поиска, замены данных.
# Используйте словарь для хранения информации.

# Словарь для хранения информации о сотрудниках
employees = {}


# Функция для добавления сотрудника
def add_employee():
    full_name = input('Введите полное имя сотрудника: ').strip()
    phone_number = input('Введите номер телефона: ').strip()
    work_email = input('Введите рабочий email: ').strip()
    position_title = input('Введите название должности: ').strip()
    office_number = input('Введите номер кабинета: ').strip()
    skype_id = input('Введите Skype ID: ').strip()

    # Создаем кортеж с информацией о сотруднике
    employee_data = (phone_number, work_email, position_title, office_number, skype_id)

    employees[full_name] = employee_data
    print(f'Сотрудник {full_name} добавлен в базу данных.')


# Функция для удаления сотрудника
def remove_employee():
    full_name = input('Введите полное имя сотрудника, которого хотите удалить: ').strip()
    if full_name in employees:
        del employees[full_name]
        print(f'Сотрудник {full_name} удален из базы данных.')
    else:
        print(f'Сотрудник {full_name} не найден в базе данных.')


# Функция для поиска сотрудника
def search_employee():
    full_name = input('Введите полное имя сотрудника, которого хотите найти: ').strip()
    if full_name in employees:
        employee_data = employees[full_name]
        print(f'Информация о сотруднике {full_name}:')
        print(f'Телефон: {employee_data[0]}')
        print(f'Рабочий email: {employee_data[1]}')
        print(f'Должность: {employee_data[2]}')
        print(f'Номер кабинета: {employee_data[3]}')
        print(f'Skype ID: {employee_data[4]}')
    else:
        print(f'Сотрудник {full_name} не найден в базе данных.')


# Функция для замены данных о сотруднике
def replace_employee():
    full_name = input('Введите полное имя сотрудника, данные которого хотите изменить: ').strip()
    if full_name in employees:
        new_phone_number = input('Введите новый номер телефона: ').strip()
        new_work_email = input('Введите новый рабочий email: ').strip()
        new_position_title = input('Введите новое название должности: ').strip()
        new_office_number = input('Введите новый номер кабинета: ').strip()
        new_skype_id = input('Введите новый Skype ID: ').strip()

        # Обновляем информацию о сотруднике
        employees[full_name] = (new_phone_number, new_work_email, new_position_title, new_office_number, new_skype_id)
        print(f'Данные сотрудника {full_name} успешно обновлены.')
    else:
        print(f'Сотрудник {full_name} не найден в базе данных.')


# Функция для отображения всех сотрудников
def display_employees():
    if employees:
        print('Список всех сотрудников:')
        for full_name, employee_data in employees.items():
            print(f'{full_name}:')
            print(f'Телефон: {employee_data[0]}')
            print(f'Рабочий email: {employee_data[1]}')
            print(f'Должность: {employee_data[2]}')
            print(f'Номер кабинета: {employee_data[3]}')
            print(f'Skype ID: {employee_data[4]}')
    else:
        print('База данных сотрудников пуста.')


# Меню для выбора действия
def menu():
    print('Меню:')
    print('1. Добавить сотрудника')
    print('2. Удалить сотрудника')
    print('3. Найти сотрудника')
    print('4. Изменить данные сотрудника')
    print('5. Показать список всех сотрудников')
    print('0. Выход')
    choice = input('Введите номер действия: ').strip()
    return choice


# Основная программа
while True:
    choice = menu()
    if choice == '1':
        add_employee()
    elif choice == '2':
        remove_employee()
    elif choice == '3':
        search_employee()
    elif choice == '4':
        replace_employee()
    elif choice == '5':
        display_employees()
    elif choice == '0':
        print('Программа завершена.')
        break
    else:
        print('Неверный выбор. Попробуйте снова.')