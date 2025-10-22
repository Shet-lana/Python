import sqlite3

# Создание соединения с базой данных
conn = sqlite3.connect('strokes.db')
cursor = conn.cursor()

# Создание таблицы для сущностей
cursor.execute('''
    CREATE TABLE IF NOT EXISTS entities (
        name TEXT PRIMARY KEY,
        type TEXT,
        age INTEGER,
        strokes_start INTEGER,
        strokes_finish INTEGER
    )
''')

# Вставка данных
cursor.execute("INSERT OR REPLACE INTO entities (name, type, age, strokes_start, strokes_finish) VALUES ('cat', 'Kuzya', 3, 0, 0)")
cursor.execute("INSERT OR REPLACE INTO entities (name, type, age, strokes_start, strokes_finish) VALUES ('human', 'Ivan', 25, 10, 10)")

# Сохранение изменений
conn.commit()

# Функция для изменения количества поглаживаний
def stroke(entity):
    if entity == 'cat':
        cursor.execute("UPDATE entities SET strokes_finish = strokes_finish + 1 WHERE name = 'cat'")
    elif entity == 'human':
        cursor.execute("UPDATE entities SET strokes_finish = strokes_finish - 1 WHERE name = 'human'")
    conn.commit()  # Сохранение изменений после каждого обновления

# Пример использования
# Получение начального количества поглаживаний у человека
cursor.execute("SELECT strokes_start FROM entities WHERE name = 'human'")
human_strokes_start = cursor.fetchone()[0]

# Цикл для изменения количества поглаживаний
for i in range(human_strokes_start):
    stroke('human')
    cursor.execute("SELECT strokes_finish FROM entities WHERE name = 'human'")
    human_strokes = cursor.fetchone()[0]
    print(f"Количество поглаживаний сделанных человеком: {human_strokes}")
    stroke('cat')
    cursor.execute("SELECT strokes_finish FROM entities WHERE name = 'cat'")
    cat_strokes = cursor.fetchone()[0]
    print(f"Количество полученных поглаживаний котом: {cat_strokes}")

# Закрытие соединения
conn.close()