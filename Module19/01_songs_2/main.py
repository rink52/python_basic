violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

full_time = 0.0
number = int(input('Сколько песен выбрать? '))
for count in range(1, number+1):
    name = input('Название {} песни: '.format(count))
    if violator_songs.get(name) is not None:
        full_time += violator_songs.get(name)
    else:
        print('Такой песни нет в списке')

print('Общее время звучания песен: {} минут '.format(round(full_time, 2)))

# не уверен насколько корректно для чистоты кода использовать "round" в "format",
# возможно эту операцию стоит сделать до "print", может быть и без нее можно
# но без нее у меня результатом выводится 14.930000000000001 минут.