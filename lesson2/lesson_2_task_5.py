def month_to_season(month):
    if 1 <= month <= 2 and 12 == month:
        return "зима"
    elif 3 <= month <= 5:
        return "весна"
    elif 6 <= month <= 8:
        return "лето"
    elif 9 <= month <= 11:
        return "осень"
    else:
        return "Неверный номер месяца"

month = int(input("Введите номер месяца (1-12): "))
print(month_to_season(month))