# Узнайте у пользователя число n.

n = int(input('Введите число: '))

# Найдите сумму чисел n + nn + nnn.

Result = str(n) + str(n + n) + str(n + n + n)

print(str(n) + "+" + str(n) + str(n) + "+" + str(n) + str(n) + str(n) + "= " + Result)
