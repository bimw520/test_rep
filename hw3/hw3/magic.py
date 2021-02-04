"""
    Магическое число.
    Необходимо угадать загаданное число за наименьшее количество попыток.

    Алгоритм:
    1. Генерируется случайное число.
    2. Пользователь вводит число.
    3. Если введенное число больше или меньше сгенерированного, то
        выводится соответствующее сообщение и возвращаемся к пункту 2.
    4. Иначе введенное число равняется сгенерированному -
        пользователь угадал число. Выводится само число и количество попыток.
        А так же вопрос "Continue? (Y/n) ".
    6. Если пользователь выбирает продолжить -
        обнуляем счетчик попыток и переходим к пункту 1.
    7. Иначе выводим сообщение 'Bye!'.

    * Для генерации случайного числа используем random.randint(-inf, +inf),
        где -inf - +inf - диапазон возможных чисел

    ** по желанию, можете хранить рекордное число попыток
    и сообщать пользователю, если он поставил новый рекорд
"""

import random

random_number = random.randint(1, 100)  # случайное число от 1 до 100

attempts_last = int(input('how much attempts: '))
attempts = 0
most_attemts = 0
print(random_number)  # if need to know

while attempts != attempts_last:
    attempts += 1
    number = int(input('enter a number: '))

    if attempts_last > most_attemts:
        most_attemts = attempts_last

    if number != random_number:
        print('wrong')

    elif number == random_number:
        print('You are WINNER!!!\n', 'Random number: ', random_number)
        print('Most attempts ', most_attemts)

    if attempts == attempts_last or number == random_number:
        if input('Continue (Y/n)') == 'Y':
            attempts_last = int(input('how much attempts: '))
            attempts = 0
            continue
        else:  #Чому в мене підчеркує після else trailing whitespaceflake8(W291)
            print('Bye')
            break
