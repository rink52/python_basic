violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

summ_time_song = 0.0

count_song = int(input('Сколько песен выбрать? '))

for i in range(count_song):
    name_song = input(f'Название {i+1} песни: ')
    for song in violator_songs:
        if name_song == song[0]:
            summ_time_song += song[1]

print(f'\nОбщее время звучания песен: {round(summ_time_song, 2)} минут')
