first = int(input('Введите число №1: '))
second = int(input('Введите  число №2: '))
third = int(input('Введите  число №3: '))
if first == second == third:
    print('Итог: 3')
elif first == second or first == third or second == third:
    print('Итог: 2')
else:
    print('Итог: 0')