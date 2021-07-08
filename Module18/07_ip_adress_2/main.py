IP = input('Введите IP: ')

verification_ip_list = IP.split('.')

for i in verification_ip_list:
    if len(verification_ip_list) != 4:
        print('Адрес - это четыре числа, разделенные точками')
        break
    elif not i.isdigit():
        print(i, 'не целое число')
        break
    elif int(i) < 0:
        print(i, 'отрицательное знаечение')
        break
    elif int(i) > 255:
        print(i, 'превышает 255')
        break
else:
    print('IP-адрес корректен')


