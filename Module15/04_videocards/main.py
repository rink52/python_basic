list_videocard = []
new_list_videocard = []

N = int(input('Кол-во видеокарт: '))
for i in range(1, N+1):
    videocard = int(input(f'{i} видеокарта: '))
    list_videocard.append(videocard)

print('\nСтарый список видеокарт: ', list_videocard)

for i in list_videocard:
    if i != max(list_videocard):
        new_list_videocard.append(i)

print('Новый список видеокарт: ', new_list_videocard)

