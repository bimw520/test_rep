"""
    Пользователь вводит начало и конец числового ряда.
    Если начало не введено - считать, что это 0.

    1. Программа считает и выводит на экран сумму числового ряда.
    2. Произведение не четных чисел числового ряда.

    * обработать возможные ошибки
"""

first_num = int(input('first num: '))

if first_num == ' ':
    first_num = 0

try:
    last_num = int(input('last num: '))

except ValueError:
    print('enter a namber')

    last_num += 1
    a = 0
    odd = 0

    for i in range(first_num, last_num):
        a += i
        if i % 2 != 0:
            odd += 1
    print('Sum = ', a)
    print('odd = ', odd)

except NameError:
    print('not defined')