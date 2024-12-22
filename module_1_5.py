# Задайте переменные разных типов данных:
immutable_var=(1,2,3,True,'test')
print(immutable_var)
print(immutable_var[1])

# Изменение значений переменных:
# immutable_var[1]=25
# TypeError: 'tuple' object does not support item assignment

# Создание изменяемых структур данных:
mutable_list=(12,15,[1,2,3],[4,5,6],['text'])
print(mutable_list)
mutable_list[2][1]=150
mutable_list[3][2]='f'
print(type(mutable_list))
mutable_list[4][0]='pic'
print(mutable_list)
