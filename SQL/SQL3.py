import sqlite3
from random import choice, randint

# CRUD - операции CRUD
connection = sqlite3.connect('DB.db')
cursor = connection.cursor()

# Удаление существующей таблицы Animal
cursor.execute('''DROP TABLE IF EXISTS Animal''')

# Создание таблицы Animal с правильным набором столбцов
cursor.execute('''CREATE TABLE IF NOT EXISTS Animal (
    id INTEGER PRIMARY KEY,
    type TEXT,
    name_id TEXT,
    age INTEGER,
    owner_id INTEGER,
    FOREIGN KEY (owner_id) REFERENCES Owner(id)
)''')

# Создание таблицы Owner
cursor.execute('''CREATE TABLE IF NOT EXISTS Owner (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    profession TEXT
)''')


# Добавление данных в таблицу Owner
cursor.execute('''INSERT INTO Owner (name, age, profession) VALUES ('Иван', 30, 'Программист')''')
cursor.execute('''INSERT INTO Owner (name, age, profession) VALUES ('Мария', 25, 'Учитель')''')
cursor.execute('''INSERT INTO Owner (name, age, profession) VALUES ('Василий', 23, 'Мерчендайзер')''')
cursor.execute('''INSERT INTO Owner (name, age, profession) VALUES ('Любовь', 32, 'Администратор')''')
cursor.execute('''INSERT INTO Owner (name, age, profession) VALUES ('Марина', 28, 'Бухгалтер')''')
cursor.execute('''INSERT INTO Owner (name, age, profession) VALUES ('Татьяна', 19, 'Специалист отдела анализа и планирования налоговых проверок')''')
cursor.execute('''INSERT INTO Owner (name, age, profession) VALUES ('Анастасия', 20, 'Хостес')''')
cursor.execute('''INSERT INTO Owner (name, age, profession) VALUES ('Елизавета', 25, 'Супервайзер')''')
cursor.execute('''INSERT INTO Owner (name, age, profession) VALUES ('Лариса', 54, 'Территориальный менеджер')''')
cursor.execute('''INSERT INTO Owner (name, age, profession) VALUES ('Василиса', 45, 'Товаровед')''')

def average_age():
    cursor.execute('''SELECT type, AVG(age) FROM Animal GROUP BY type''')
    ages = cursor.fetchall()

    print(len(ages))
    print(ages)
    for age in ages:
        print(age)

def create_record():
    cursor.execute('''INSERT INTO Animal (
        type,
        age,
        owner_id
    ) VALUES (?, ?, ?)''', ('млекопитающее', 15, 1))

def delete_IVASIK():
    cursor.execute('''DELETE FROM Animal WHERE id = 2''')

def update_IVASIK():
    cursor.execute('''UPDATE Animal SET age = 4 WHERE id = 1''')

def read_IVASIK():
    cursor.execute('''SELECT * FROM Animal''')
    animals = cursor.fetchall()
    print(animals)

def randomizer():
    types = ['млекопитающее', 'птица', 'рыба', 'рептилия', 'насекомое']
    for _ in range(500):
        animal_type = choice(types)
        animal_age = randint(1, 20)
        owner_id = randint(1, 10)
        # Генерируем случайное имя животного
        names = ["Барсик", "Шарик", "Рекс", "Том", "Джерри"]
        name_id = choice(names)

        cursor.execute('''INSERT INTO Animal (
            type,
            age,
            name_id,
            owner_id
        ) VALUES (?, ?, ?, ?)''', (animal_type, animal_age, name_id, owner_id))

def remove_duplicates():
    cursor.execute('''
        DELETE FROM Animal
        WHERE id NOT IN (
            SELECT MIN(id)
            FROM Animal
            GROUP BY type, age, owner_id
        )
    ''')

# Вызов функции randomizer для заполнения таблицы Animal
randomizer()

# Вызов функции remove_duplicates для удаления дубликатов
remove_duplicates()

# Вызов функции average_age для вычисления среднего возраста
average_age()

connection.commit()
connection.close()