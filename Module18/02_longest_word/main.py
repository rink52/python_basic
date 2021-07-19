text = 'я узнал что у меня есть огромная семья'
list_text = text.split(' ')

longest_word = max(list_text, key=len)

print('Самое длинное слово: ', longest_word)
print('Его длинна {} символов'.format(len(longest_word)))