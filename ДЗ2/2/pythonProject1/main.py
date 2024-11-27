# Ввод данных от пользователя
zarplata = float(input("Введите вашу зарплату за месяц: "))
kredit = float(input("Введите сумму ежемесячного платежа по кредиту: "))
komunalnye = float(input("Введите сумму задолженности за коммунальные услуги: "))

# Рассчитываем оставшуюся сумму после всех выплат
ostatochnaya_summa = zarplata - kredit - komunalnye

# Выводим результат на экран
if ostatochnaya_summa >= 0:
    print(f"После всех выплат у вас останется {ostatochnaya_summa:.2f} рублей.")
else:
    print(f"Вам не хватает {abs(ostatochnaya_summa):.2f} рублей для покрытия всех расходов.")
