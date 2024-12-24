# Расчет среднего балла для студентов
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
summend = {}
students = list(students)  # Преобразование множества в список
# print(students)
students.sort()  # Сортировка списка студентов по алфавиту
# print(students)

# print('Сумма оценок студента ',sum(grades[0]))
# print('Количество оценок студента ',len(grades[0]))
# print('Средний бал студента ',sum(grades[0])/len(grades[0]))



for i in range (len(students)):
    summend[students[i]] = sum(grades[i]) / len(grades[i])


print('Средний балл студентов: ',summend)
