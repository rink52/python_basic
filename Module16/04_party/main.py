guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    question = input('\nГость пришел или ушел? ')
    if question.lower() != 'пора спать':
        print(f'Сейчас на вечеринке {len(guests)} человек: ', guests)
        name = input('Имя гостя: ')
        if question.lower() == 'пришел' or question.lower() == 'пришёл':
            if len(guests) < 6:
                print(f'Привет, {name}!')
                guests.append(name)
            else:
                print(f'Прости, {name}, но мест нет.')
        elif question.lower() == 'ушел' or question.lower() == 'ушёл':
            if guests.count(name) > 0:
                print(f'Пока, {name}!')
                guests.remove(name)
            else:
                print(f'{name} сейчас не присутствует на вечеринке! ')
        else:
            print('Ошибка ввода, попробуйте снова! ')
    else:
        break

print('\nВечеринка закончилась, все легли спать.')






