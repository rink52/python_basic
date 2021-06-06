list_word = list(input('Введите слово: ').lower())
matching_values = 0

for ch in range(len(list_word) // 2):
    if list_word[ch] == list_word[len(list_word) - (ch+1)]:
        matching_values += 1
    else:
        break

if matching_values == len(list_word) // 2:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
