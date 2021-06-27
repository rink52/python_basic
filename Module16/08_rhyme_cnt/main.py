players = int(input('Кол-во человек: '))
number_kick = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {number_kick} человек')
players = list(range(1, count_players+1))

index_del = 0

while len(players) > 1:
    print('\nТекущий круг людей:', players)
    index_start = index_del % len(players)
    print('Начало счёта с номера', players[index_start])

    index_del = (index_start + number_kick - 1) % len(players)
    print('Выбывает человек под номером', players[index_del])
    players.remove(players[index_del])

print('\nОстался человек под номером', players[0])




