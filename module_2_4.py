# Программа Всё не так уж просто. Цикл for. Элементы списка. Полезные функции в цикле.
print('Всё не так уж просто')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []   # только Простые числа
not_primes = [] # все Не Простые числа
for n in range(2, len(numbers)):
    count = 0
    delitel = 2
    while delitel < n:
        if n % delitel == 0:
            count = count + 1
        delitel = delitel + 1

    if count == 0:
        primes.append(n)
not_primes = [x for x in numbers if x not in primes]
del not_primes[0]
print('Сложные числа: ','not_primes = ', not_primes)
print('Простые числа: ','primes = ', primes)
