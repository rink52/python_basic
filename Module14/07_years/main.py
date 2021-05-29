first_year = int(input('Введите первый год: '))
second_year = int(input('Введите второй год: '))
answer = []
for year in range(first_year, second_year + 1):
    str_year = str(year)
    set_str_year = set(str_year)
    for ch in set_str_year:
        if str_year.count(ch) == 3:
            answer.append(year)

print(f'Годы от {first_year} до {second_year} с тремя одинаковыми цифрами:')
print(*answer, sep='\n')


