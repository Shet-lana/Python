import datetime
from collections import defaultdict

# Данные
transactions = [] # Список транзакций
categories = ['Зарплата', 'Подарки', 'Продукты', 'Транспорт', 'Развлечения'] # Категории расходов/доходов
data_file = 'finance_data.txt' # Файл с данными

# Загрузка данных из файла
try:
    with open(data_file, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            date = datetime.datetime.strptime(data[0], '%Y-%m-%d').date()
            amount = float(data[1])
            category = data[2]
            transactions.append({'date': date, 'amount': amount, 'category': category})
except FileNotFoundError:
    pass # Если файл не найден, оставляем список пустым

# Сохранение данных в файл
def save_data():
    with open(data_file, 'w') as file:
        for transaction in transactions:
            date_str = transaction['date'].strftime('%Y-%m-%d')
            amount_str = str(transaction['amount'])
            category = transaction['category']
            file.write(f'{date_str},{amount_str},{category}\n')

# Добавление новой транзакции
def add_transaction(amount, category):
    today = datetime.date.today()
    transactions.append({'date': today, 'amount': amount, 'category': category})
    save_data()

# Получение статистики за месяц
def get_monthly_statistics(month=None):
    if not month:
        now = datetime.datetime.now()
        month = now.month
        year = now.year
    transactions_in_month = [t for t in transactions if t['date'].month == month and t['date'].year == year]
    income = sum(t['amount'] for t in transactions_in_month if t['amount'] > 0)
    expenses = abs(sum(t['amount'] for t in transactions_in_month if t['amount'] < 0))
    balance = income - expenses
    return {'income': income, 'expenses': expenses, 'balance': balance}

# Расчет накоплений
def calculate_savings():
    savings = sum(t['amount'] for t in transactions if t['amount'] > 0) - \
              abs(sum(t['amount'] for t in transactions if t['amount'] < 0))
    return savings

# Предложения категорий
def suggest_categories():
    existing_categories = set([t['category'] for t in transactions])
    suggestions = [c for c in categories if c not in existing_categories]
    return suggestions

# Формирование отчета
def show_report():
    report = defaultdict(int)
    for transaction in transactions:
        report[(transaction['date'], transaction['category'])] += transaction['amount']
    for key, value in sorted(report.items()):
        date, category = key
        print(f"{date.strftime('%Y-%m-%d')} | {category}: {value:.2f}")

# Основной цикл программы
while True:
    print("\nМеню:")
    print("1. Добавить доход")
    print("2. Добавить расход")
    print("3. Просмотреть месячную статистику")
    print("4. Рассчитать накопления")
    print("5. Рекомендации по категориям")
    print("6. Сформировать отчёт")
    print("7. Завершить работу")

    choice = input("Выберите пункт меню: ")

    if choice == '1':
        amount = float(input("Введите сумму дохода: "))
        category = input("Введите категорию дохода: ")
        add_transaction(amount, category)
        print("Доход успешно добавлен!")
    elif choice == '2':
        amount = float(input("Введите сумму расхода: "))
        category = input("Введите категорию расхода: ")
        add_transaction(-amount, category)
        print("Расход успешно добавлен!")
    elif choice == '3':
        statistics = get_monthly_statistics()
        print(f"Доход: {statistics['income']:.2f}, Расходы: {statistics['expenses']:.2f}, Баланс: {statistics['balance']:.2f}")
    elif choice == '4':
        savings = calculate_savings()
        print(f"Ваши накопления составляют: {savings:.2f}")
    elif choice == '5':
        suggestions = suggest_categories()
        print("Рекомендованные категории:", ', '.join(suggestions))
    elif choice == '6':
        show_report()
    elif choice == '7':
        break # Выход из цикла