# Домашняя работа по уроку "Пространство имён"

calls = 0   # Глобальная переменная для подсчета вызовов функций

def count_calls():  # Функция для подсчета вызовов
    global calls
    calls += 1

def string_info(string):    # Функция для получения информации о строке
    count_calls()  # Увеличиваем счетчик вызовов

    length = len(string)    # Получаем информацию о строке
    upper_case = string.upper()
    lower_case = string.lower()

    return length, upper_case, lower_case

def is_contains(string, list_to_search):    # Функция для проверки наличия строки в списке
    count_calls()  # Увеличиваем счетчик вызовов

    string_lower = string.lower()   # Приводим все к одному регистру для сравнения
    list_to_search_lower = [item.lower() for item in list_to_search]

    return string_lower in list_to_search_lower

print(string_info('Capybara'))  # Пример 1
print(string_info('Armageddon'))  # Пример 2
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Пример 3
print(is_contains('cycle', ['recycling', 'cyclic']))  # Пример 4

print('Количество вызовов функций ',calls)  # Количество вызовов функций