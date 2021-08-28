def check_digit(input):                                         # Функция проверки ввода на числа
    for symbol in input:
        if symbol.isdigit() == False:
            return False

import random
n = int(input("Введите максимальное число: "))
secret_number = random.randint(0, n)                            #генерим число загаданное Артемом
numbers = set(range(0, n+1))                                    #создаем множество чисел от 0 до максимального

while True:
    input_numbers = set(input("Нужное число есть среди вот этих чисел: ").split(" "))

    if input_numbers == {"Помогите!"}:                          #проверяем на ввод контрольного слова
        print("Артём мог загадать следующие числа:", end=" ")
        print(*numbers)
    elif check_digit(input_numbers) == False:                   # проверка ввода на числа
        print("Ошибка ввода. Попробуйте снова")
        continue
    else:
        input_numbers = set(map(int, input_numbers))                   #преобразуем в нашем множестве с строки в числовые занчения

        if secret_number in input_numbers and len(input_numbers) == 1:      # Если введенное значение только одно проваеряем наше ли это число
            print("Число угадано верно! ")
            break
        elif secret_number in input_numbers:
            print("Ответ Артёма: Да")
            numbers = input_numbers
        else:
            print("Ответ Артёма: Нет")
            numbers -= input_numbers
