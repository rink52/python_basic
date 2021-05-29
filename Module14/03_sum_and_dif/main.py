def summ(number):
    summ_number = 0
    while number > 0:
        last_number = number % 10
        summ_number += last_number
        number //= 10
    return summ_number

def quantity(number):
    quantity_number = 0
    while number > 0:
        last_number = number % 10
        quantity_number += 1
        number //= 10
    return quantity_number


number = int(input('Введите число: '))

difference = summ(number) - quantity(number)

print('\nСумма цифр: ', summ(number))
print('Кол-во цифр в числе: ', quantity(number))
print('Разность суммы и кол-ва цифр: ', difference)


#Но проще было сделать даже без отдельных функций

# while number > 0:
#     last_number = number % 10
#     summ_number += last_number
#     quantity_number += 1
#     number //= 10