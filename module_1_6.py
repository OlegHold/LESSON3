# Работа со словарями:
my_dict={'Люба':31101953,'Саша':10101957,'Оксана':13101973}
print('Dict :',my_dict)
print('Existing value:',my_dict['Саша'])
print('Not existing value:',my_dict.get('Олеся'))
my_dict['Ирина']=15031954
my_dict['Женя']=10091997
my_dict['Вова']=29101999
print('Deleted value: ',my_dict['Ирина'])
del my_dict['Ирина']
# print(my_dict['Ирина'])  KeyError: 'Ирина' File "E:\_PythonProject\Lesson\module_1_6.py", line 10, in <module>
print('Modified dictionary: ',my_dict)

# Работа с множествами:
my_set={1,2,3,4,5,1,2,3,'one','two','three','one','two',3.1459}
print('Set',my_set)
print(my_set.add(120))
print(my_set.add(150))
print(my_set)
print(my_set.discard(2))
print('Modified set: ',my_set)

