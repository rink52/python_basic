size_list = []
human_foot_size_list = []
count_human_to_skate = 0

count_skate = int(input('\nКол-во коньков: '))
for size_skate in range(1, count_skate+1):
    size_list.append(input(f'Размер {size_skate} пары: '))

count_human = int(input('\nКол-во людей: '))
for size_foot in range(1, count_human+1):
    human_foot_size_list.append(input(f'Размер ноги {size_foot} человека: '))

for size_skate in human_foot_size_list:
    if size_list.count(size_skate) > 0:
        size_list.remove(size_skate)
        count_human_to_skate += 1

print('\nНаибольшее кол-во людей, которые могут взять ролики: ', count_human_to_skate)