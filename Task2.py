# Пользователь вводит время в секундах.

User_Seconds = int(input('Введите количество секунд: '))

# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.

Hourse = str(User_Seconds//3600)
Minutes = (User_Seconds // 60) % 60
Seconds = User_Seconds % 60

# Используйте форматирование строк.

if Minutes < 10:
    Minutes = '0' + str(Minutes)
else:
    Minutes = str(Minutes)
if Seconds < 10:
    Seconds = '0' + str(Seconds)
else:
    Seconds = str(Seconds)

print(Hourse + ':' + Minutes + ':' + Seconds)
