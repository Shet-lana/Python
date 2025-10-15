import sqlite3
from random import choice, randint

# CRUD - операции CRUD
connection = sqlite3.connect('DB.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Animal (
    id INTEGER PRIMARY KEY,
    type TEXT,
    name TEXT,
    age INTEGER
)''')

def create_record():
    cursor.execute('''INSERT INTO Animal (
        type,
        name,
        age
    ) VALUES (?, ?, ?)''', ('млекопитающее', 'мяу', 15))
    create_record()

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

randomizer()

connection.commit()
connection.close()