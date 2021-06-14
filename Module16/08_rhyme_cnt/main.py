def laps(players, shift_element_list):
    print('\nТекущий круг людей: ', sorted(players))
    print('Начало счета с номера: ', players[0])
    print('Выбывает человек под номером: ', shift_element_list[0])
    shift_element_list.pop(0)
    players.clear()
    return players

count_players = int(input('Кол-во человек: '))
number_kick = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {number_kick} человек')
players = list(range(1, count_players+1))

while len(players) != 1:
    shift_element_list = []

    if len(players) >= number_kick:
        for i in range(len(players)):
            if (number_kick + i ) <= len(players):
                shift_element_list.append(players[number_kick - 1 + i])
            else:
                for i in range(number_kick-1):
                    shift_element_list.append(players[i])
                laps(players, shift_element_list)
                players = shift_element_list.copy()
                break

    elif len(players) < number_kick and number_kick // len(players) == 1:
        for i in range(len(players)):
            if (number_kick - len(players) - 1 + i) < len(players):
                shift_element_list.append(players[(number_kick - len(players) - 1 + i)])
                if len(players) == len(shift_element_list):
                    laps(players, shift_element_list)
                    players = shift_element_list.copy()
                    break
            else:
                for i in range(number_kick - len(players) - 1):
                    shift_element_list.append(players[i])
                laps(players, shift_element_list)
                players = shift_element_list.copy()
                break
    else:
        for i in range(len(players)):
            shift_element_list.append(players[(number_kick % len(players) - 1 + i)])
        laps(players, shift_element_list)
        players = shift_element_list.copy()

print(f'\nОстался человек под номером {players[0]}')




