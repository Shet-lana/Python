# Создайте программу, хранящую информацию о великих баскетболистах.
# Нужно хранить ФИО баскетболиста и его рост. Требуется реализовать возможность
# добавления, удаления, поиска, замены данных. Используйте словарь
# для хранения информации.


def add_player(players, full_name, height):
    """
    Добавляет нового игрока в словарь players.
    :param players: Словарь, где хранятся игроки.
    :param full_name: Полное имя игрока.
    :param height: Рост игрока.
    """
    if full_name in players:
        print(f'Игрок {full_name} уже существует.')
    else:
        players[full_name] = {'height': height}
        print(f'Игрок {full_name} добавлен успешно.')

def remove_player(players, full_name):
    """
    Удаляет игрока из словаря players.
    :param players: Словарь, где хранятся игроки.
    :param full_name: Полное имя игрока.
    """
    if full_name in players:
        del players[full_name]
        print(f'Игрок {full_name} удалён успешно.')
    else:
        print(f'Игрок {full_name} не найден.')

def search_player(players, full_name):
    """
    Ищет игрока в словаре players и возвращает его данные.
    :param players: Словарь, где хранятся игроки.
    :param full_name: Полное имя игрока.
    :return: Данные игрока или None, если игрок не найден.
    """
    return players.get(full_name, None)

def update_player_height(players, full_name, new_height):
    """
    Обновляет рост игрока в словаре players.
    :param players: Словарь, где хранятся игроки.
    :param full_name: Полное имя игрока.
    :param new_height: Новый рост игрока.
    """
    if full_name in players:
        players[full_name]['height'] = new_height
        print(f'Рост игрока {full_name} обновлён до {new_height}.')
    else:
        print(f'Игрок {full_name} не найден.')


# Создание пустого словаря для хранения игроков
players = {}

# Добавление игроков
add_player(players, 'Иванов Иван Иванович', 198)
add_player(players, 'Сидоров Иван Иванович', 201)
add_player(players, 'Петров Иван Иванович', 206)

# Поиск игрока
player_data = search_player(players, 'Иванов Иван Иванович')
if player_data:
    print(f'Найден игрок: {player_data}')
else:
    print('Игрок не найден.')

# Обновление роста игрока
update_player_height(players, 'Петров Иван Иванович', 208)

# Удаление игрока
remove_player(players, 'Сидоров Иван Иванович')