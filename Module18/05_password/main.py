lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number_list = '1234567890'
lower_upper_number_count = [0,0,0]

while True:
    password = input('Придумайте пароль: ')
    if len(password) < 8:
        print('Пароль слишком короткий. Попробуйте еще раз.')
        break
    else:
        for symbol in password:
            if lower_alphabet.find(symbol) != -1:
                lower_upper_number_count[0] += 1
            elif upper_alphabet.find(symbol) != -1:
                lower_upper_number_count[1] += 1
            elif number_list.find(symbol) != -1:
                lower_upper_number_count[2] += 1
            else:
                print('Недопустимый символ')
                break

        if lower_upper_number_count[0] > 0 and lower_upper_number_count[1] > 0 and lower_upper_number_count[2] >= 3:
            print('Это надёжный пароль!')
            break
        else:
            print('Пароль ненадёжный. Попробуйте ещё раз.')
            lower_upper_number_count = [0, 0, 0]

