"""
    (1-3 пункты были решены на уроке, необходимо привести все к нужному виду)

    При запуске программы выбор:
    1. Найти количество четных и нечетных цифр числа.
    2. Найти факториал числа.
    3. Вывести последовательность чисел в степени до предела.
    4. Выход.

    * после выполнения пунктов 1-3 попадаем обратно в меню.
"""
while True:
    a = print('1. Найти количество четных и нечетных цифр числа.')
    b = print('2. Найти факториал числа.')
    c = print('3. Вывести последовательность чисел в степени до предела.')
    d = print('4. Выход.')
    numb_operation = int(input('Insert a number: '))
    
    if numb_operation == "1":
        even = 0
        odd = 0
        print(a, '\n')
        number = int(input("insert a number: "))
        while number > 0:  # пока число больше 0 заходим в цикл
            last_digit = number % 10  # получаем последнюю цифру числа

            if last_digit % 2 == 0:  # если кратное двум - четное
                even += 1  # увеличиваем счетчик четных
            else:
                odd += 1  # увеличиваем счетчик нечетных чисел
                print("even:", even)
                print("odd:", odd)
        continue

    elif numb_operation == "2":
        print(a, '\n')
        number = int(input("insert a number: "))
        factorial = 1

        while number > 1:
            factorial *= number
            number -= 1
            print(factorial)
        continue

    elif numb_operation == "3":
        p = int(input("Введите степень: "))
        limit = int(input("Предел: "))
        number = 1

        while (result := number ** p) < limit:
            print(result)
            number += 1
        continue
    elif numb_operation == "4":
        print('Bye')
        break
