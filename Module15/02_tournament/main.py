name_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
print('Список всех участников', name_list)

participant_list_day1 = []
participant_list_day2 = []

for i in range(len(name_list)):
    if (i+1) % 2 == 0:
        participant_list_day1.append(name_list[i])
    else:
        participant_list_day2.append(name_list[i])

print('\nСписок участников в 1 день:', participant_list_day1)
print('Список участников во 2 день:', participant_list_day2)

#решил все же доделать на 2 дня :)