vowel_letters = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
text = input('Введите текст: ')

list_count_letters = [letter for letter in text if (letter in vowel_letters)]

print('Список гласных букв: ', list_count_letters)
print('Длина списка: ', len(list_count_letters))

