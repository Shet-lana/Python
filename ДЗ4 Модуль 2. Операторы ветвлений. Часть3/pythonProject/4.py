# Задание 4
# Зарплатаменеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше
# 1000 — 8%. Пользователь вводит с клавиатуры уровень
# продаж для трех менеджеров. Определить их зарплату,
# определить лучшего менеджера, начислить ему премию
# 200$, вывести итоги на экран.

def calculate_salary(sales):
    salary = 200  # базовая зарплата
    if sales <= 500:
        bonus = sales * 0.03  # 3% от продаж
    elif sales <= 1000:
        bonus = sales * 0.05  # 5% от продаж
    else:
        bonus = sales * 0.08  # 8% от продаж
    return salary + bonus


def find_best_manager(manager_sales):
    best_index = 0
    max_sales = manager_sales[best_index]
    for i in range(len(manager_sales)):
        if manager_sales[i] > max_sales:
            best_index = i
            max_sales = manager_sales[i]
    return best_index


def main():
    manager_sales = []
    for i in range(3):
        sales = float(input(f'Уровень продаж для менеджера {i + 1}: '))
        manager_sales.append(sales)

    salaries = []
    for sales in manager_sales:
        salary = calculate_salary(sales)
        salaries.append(salary)

    best_index = find_best_manager(manager_sales)
    best_salary = salaries[best_index] + 200  # премия 200$
    salaries[best_index] = best_salary

    for i in range(3):
        print(f'Зарплата менеджера {i + 1}: ${salaries[i]:.2f}')


if __name__ == "__main__":
    main()
