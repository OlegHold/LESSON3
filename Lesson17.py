# Домашняя работа по Модуль 2. Основные операторы

def generate_password(n):  # определяем функцию
    password = ""  # пустая строка для хранения пар чисел (пароль)

    for i in range(1, 21):  # Внешний цикл проходит по каждому первому числу i от 1 до 20
        for j in range(i + 1, 21):   # Внутренний цикл выбирает второе число j, начиная с i+1, чтобы избежать повторений
            # формируем пару
            pair_sum = i + j   # Для каждой уникальной пары чисел считается их сумма: pair_sum = i+j

            # проверка кратности
            if pair_sum > 0 and n % pair_sum == 0: # Если сумма положительная и число n делится на сумму без остатка, добавляем пару в строку пароля
                password += str(i) + str(j)

    return password


for i in range(3, 21):
    result = generate_password(i)
    print(f"{i} - {result}")