text = 'тестовая строка h h ьсоличулоп ьтунревереп h и все рады'
# text = input('Введите текст: ')

str_text = [cnt
            for cnt in range(len(text))
            if text[cnt] == 'h']

text_new = text[:str_text[0]] + text[str_text[-1]:str_text[0]:-1] + text[str_text[-1]:]

print(text_new)