# Запрашиваем у пользователя ввод трехзначного числа
number = int(input("Введите трехзначное число: "))

# Проверяем, что число является трехзначным
if 100 <= number <= 999:
    # Извлекаем цифры числа
    a = number // 100         # Сотни
    b = (number // 10) % 10   # Десятки
    c = number % 10           # Единицы

    # Находим сумму цифр
    sum_of_digits = a + b + c

    # Выводим результат
    print("Сумма цифр числа:", sum_of_digits)
else:
    print("Ошибка: введено не трехзначное число")