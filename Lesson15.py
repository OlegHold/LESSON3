# "Матрица воплоти"
def get_matrix (n, m, value):  # n строк и m столбцов, значения value
    matrix = []
    for i in range(n):
        matrix.append([]) # добавляем список в строчку i
        for j in range(m):
            matrix[i].append(value) # Пишем в список значение строчки i столбца j
    print(matrix)
get_matrix(2, 2, 10)
get_matrix(3, 5, 42)
get_matrix(4, 2, 13)
print('Расчет окончен')