N = int(input('Сколько будет чисел: '))
list_number = [int(input(f'Введите {cnt+1} число: '))
               for cnt in range(N)]
print('\nВведенный список: ', list_number)

for number in range(list_number.count(0)):
    list_number.remove(0)
    list_number.append(0)
print('Сортированный список: ', list_number)

# как можно сократить запись с последовательным
# применением методов к списку, в одну строчку
# чтоб была запись типо list_number.remove(0) .append(0) ?


del list_number[len(list_number) - list_number.count(0):]
print('Сжатый список: ', list_number)


