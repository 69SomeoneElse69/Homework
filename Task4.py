# Пользователь вводит целое положительное число.

Number = int(input("Введите положительное число: "))

# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

max = Number % 10
Number = Number // 10

while Number > 0:
    if Number % 10 > max:
        max = Number % 10
    Number = Number // 10

print('Самая большая цифра в числе: ' + str(max))

