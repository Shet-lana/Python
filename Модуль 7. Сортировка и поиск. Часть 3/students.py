import pandas as pd

# 1. Чтение данных из CSV файла
data = pd.read_csv('students.csv')

# Просмотр первых пяти строк:
print('Первые 5 строк:')
print(data.head())

# 2. Основная информация:
print('\nОбщая информация:')
data.info()

# Определение количества строк и столбцов:
print(f'\nКоличество строк: {data.shape[0]}')
print(f'\nКоличество столбцов: {data.shape[1]}')

# 3. Фильтрация данных :
older_than_21 = data[data['Age'] > 21]
print('\nСтарше 21 года:')
print(older_than_21)

print('\nСтуденты из Москвы:')
print(data.query("City == 'Moscow'"))

# 4. Расчет статистики :

avg_grade = data['Grade'].mean()
max_grade = data['Grade'].max()
min_grade = data['Grade'].min()
print('\nСтатистика по баллам:')
print(f'Средний балл: {avg_grade}')
print(f'Максимальный балл: {max_grade}')
print(f'Минимальный балл: {min_grade}')

# 5. Добавление нового столбца :
status_values = []
for grade in data['Grade']:
    if grade >= 85:
        status_values.append('Passed')
    else:
        status_values.append('Failed')
data['Status'] = status_values

# 6. Сохранение данных :
data.to_csv('students_updated.csv', index=False)

