message = input('Сообщение: ')
word_list = message.split(' ')
word = ''

print('Новое сообщение: ', end='')
for i in word_list:
    if i.isalpha() or i.isdigit():
        print(i[::-1], end=' ')
    else:
        for sym in i:
            if sym.isalpha() or sym.isdigit():
                word += sym
            else:
                print(word[::-1] + sym, end='')
                word = ''
        print(word[::-1] + sym, end=' ')
        word = ''


