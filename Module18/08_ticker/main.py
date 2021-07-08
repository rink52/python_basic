first_string = input('Первая строка: ')
second_string = input('Вторая строка: ')

for i in range(len(second_string)):
    if first_string == second_string:
        print('Строки равны.')
        break
    elif second_string[i:] + second_string[:i] == first_string:
        print(f'Первая строка получается из второй со сдвигом {len(second_string)-i}.')
        break
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
