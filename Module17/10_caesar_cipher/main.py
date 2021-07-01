abc = ['а','б','в','г','д','е','ё','ж',
       'з','и','й','к','л','м','н','о',
       'п','р','с','т','у','ф','х','ц',
       'ч','ш','щ','ъ','ы','ь','э','ю','я']

text = (input('Введите сообщение: ')).lower()
shift = int(input('Введите сдвиг: '))
encrypt_text = ''
for symbol in text:
    if symbol == ' ':
        encrypt_text += symbol
    else:
        encrypt_text += abc[(abc.index(symbol)+shift) % len(abc)]

print('Зашифрованное сообщение: ', encrypt_text)

