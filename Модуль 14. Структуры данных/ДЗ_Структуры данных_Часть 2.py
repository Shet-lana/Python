class UserManager:
    def __init__(self):
        self.users = {}

    @staticmethod
    def _is_valid_password(password):
        """
        Проверяет пароль на соответствие правилам безопасности:
        - Минимум 8 символов
        - Содержит хотя бы одну заглавную букву
        - Содержит хотя бы одну цифру
        """
        return (
            len(password) >= 8 and
            any(char.isupper() for char in password) and
            any(char.isdigit() for char in password)
        )

    def add_user(self):
        """Добавляет нового пользователя"""
        while True:
            login = input('Введите новый логин (минимум 4 символа): ').strip()
            if len(login) < 4:
                print('Логин должен содержать минимум 4 символа.')
                continue
            if login in self.users:
                print(f'Пользователь {login} уже существует.')
                continue
            break

        while True:
            password = input('Введите пароль (минимум 8 символов, включающих заглавную букву и цифру): ')
            if not self._is_valid_password(password):
                print('Пароль не соответствует требованиям безопасности.')
            else:
                self.users[login] = password
                print(f'Пользователь {login} успешно добавлен.')
                break

    def remove_user(self):
        """Удаляет существующего пользователя"""
        login = input('Введите логин пользователя для удаления: ')
        if login not in self.users:
            print(f'Пользователь {login} не найден.')
        else:
            del self.users[login]
            print(f'Пользователь {login} удалён.')

    def check_user(self):
        """Проверяет существование пользователя"""
        login = input('Введите логин для проверки: ')
        if login in self.users:
            print(f'Пользователь {login} существует.')
        else:
            print(f'Пользователь {login} отсутствует.')

    def change_login(self):
        """Изменяет логин существующего пользователя"""
        old_login = input('Введите старый логин: ')
        if old_login not in self.users:
            print(f'Пользователь {old_login} не найден.')
        else:
            new_login = input('Введите новый логин (минимум 4 символа): ').strip()
            if len(new_login) < 4:
                print('Новый логин должен содержать минимум 4 символа.')
            elif new_login in self.users:
                print(f'Логин {new_login} уже занят.')
            else:
                self.users[new_login] = self.users.pop(old_login)
                print(f'Логин обновлён на {new_login}.')

    def change_password(self):
        """Изменяет пароль существующего пользователя"""
        login = input('Введите логин пользователя для изменения пароля: ')
        if login not in self.users:
            print(f'Пользователь {login} не найден.')
        else:
            current_password = self.users.get(login)
            while True:
                new_password = input('Введите новый пароль (минимум 8 символов, включающих заглавную букву и цифру): ')
                if new_password == current_password:
                    print('Пароль должен отличаться от ранее созданного.')
                elif not self._is_valid_password(new_password):
                    print('Пароль не соответствует требованиям безопасности.')
                else:
                    self.users[login] = new_password
                    print(f'Пароль для пользователя {login} обновлён.')
                    break


if __name__ == "__main__":
    user_manager = UserManager()

    while True:
        print('\n Меню ')
        print('1. Добавить нового пользователя')
        print('2. Удалить существующего пользователя')
        print('3. Проверить существует ли пользователь')
        print('4. Изменить логин существующего пользователя')
        print('5. Изменить пароль существующего пользователя')
        print('6. Выход')

        choice = input('Выберите пункт меню: ')

        if choice == '1':
            user_manager.add_user()
        elif choice == '2':
            user_manager.remove_user()
        elif choice == '3':
            user_manager.check_user()
        elif choice == '4':
            user_manager.change_login()
        elif choice == '5':
            user_manager.change_password()
        elif choice == '6':
            break
        else:
            print('Неверный выбор. Попробуйте снова.')