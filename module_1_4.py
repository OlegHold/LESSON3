#Программа подсчета символов в строке
print("Программа подсчета символов в строке")
print("Пожалуйста введите любое слово:")
my_string=input()
print("В вашем слове содержится ",len(my_string)," символов.")

#Работа с методами строк
my_string= "test words and numbers"
print(my_string.upper())
print(my_string.upper().lower())
print(type(my_string))

print(my_string.replace(" ",""))

print(my_string[0])
print(my_string[-1])

