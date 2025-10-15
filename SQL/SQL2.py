import sqlite3
from random import choice, randint

# CRUD - операции CRUD
connection = sqlite3.connect('DB.db')
cursor = connection.cursor()

# Создание таблицы Animal
cursor.execute('''CREATE TABLE IF NOT EXISTS Animal (
    id INTEGER PRIMARY KEY,
    type TEXT,
    name TEXT,
    age INTEGER
)''')

# Создание таблицы Owner
cursor.execute('''CREATE TABLE IF NOT EXISTS Owner (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    profession TEXT
)''')

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
        name,
        age
    ) VALUES (?, ?, ?)''', ('млекопитающее', 'мяу', 15))

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
    names = ['Кузя', 'Нюся', 'Пушок', 'Рекс', 'Жужа', 'Мурка']
    for _ in range(500):
        animal_type = choice(types)
        animal_name = choice(names)
        animal_age = randint(1, 20)
        cursor.execute('''INSERT INTO Animal (
            type,
            name,
            age
        ) VALUES (?, ?, ?)''', (animal_type, animal_name, animal_age))

def remove_duplicates():
    cursor.execute('''
        DELETE FROM Animal
        WHERE id NOT IN (
            SELECT MIN(id)
            FROM Animal
            GROUP BY type, name, age
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