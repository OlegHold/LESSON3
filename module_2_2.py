# Программа поиска и подсчета одинаковых чисел
print('Необходимо ввести 3 целых числа')
print(' ')

print('Введите первое число: ')
first = input()

print('Введите второе число: ')
second = input()

print('Введите третье число: ')
third = input()

i=0
if first == second or first == third or second == third:
    i = 2
if second == third == first:
    i = 3
print('Одинаковых чисел: ', i)


