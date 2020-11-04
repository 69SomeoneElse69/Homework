# Поработайте с переменными,
# создайте несколько,
# выведите на экран,

Number = int(input('введите число: '))
String = str(input('Введите строку: '))
print(Number, String)

# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

Number1 = int(input('Введите первое число'))
Number_Assembler = Number1
Number1 = int(input('Введите второе число'))
Number_Assembler = (str(Number_Assembler) + ' ' + str(Number1))

String1 = str(input('Введите первую строку'))
String_Assembler = String1
String1 = str(input('Введите вторую строку'))
String_Assembler = String_Assembler + ' ' + String1

print(Number_Assembler)
print(String_Assembler)