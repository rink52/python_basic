list_word = list(input('Введите слово: '))
unique_letters = 0

for ch in list_word:
    count_symbol = 0
    for symbol in list_word:
        if ch.lower() == symbol.lower():
            count_symbol += 1

    if count_symbol <= 1:
        unique_letters += 1

print('Кол-во уникальных букв: ', unique_letters)

#Подумал что в случае с поиском одинаковых букв регистр не должен иметь значения, поэтому применил lower.