file_name = input('Введите имя файла: ')

# if file_name.startswith(('@','№','$','%','^','&','*','(',')')) == True:
#Или можно так

invalid_characters = '@№$%^&*()'
if invalid_characters.find(file_name[0]) != -1:

    print('Ошибка: название начинается на один из специальных символов')
elif not file_name.endswith(('.txt', '.docx')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно.')
