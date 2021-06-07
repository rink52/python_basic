import nltk

def compare(s1, s2):
    return nltk.edit_distance(s1, s2) / ((len(s1) + len(s2)) / 2)

def add_film_favorite(i):
    favorite_film_list.append(i)
    print(f'Фильм "{i}" добавлен в избранное')


films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

favorite_film_list = ['']

while True:
    favorite_film = input('\nВведите название фильма: ')
    a = False
    for i in films:
        if favorite_film.lower() == i.lower() or compare(favorite_film.lower(), i.lower()) < 0.4:
            for ch in favorite_film_list:
                if favorite_film_list[0] == '':
                    favorite_film_list.remove(favorite_film_list[0])
                    add_film_favorite(i)
                elif i.lower() != ch.lower():
                    add_film_favorite(i)
                else:
                    print(f'Фильм "{i}" уже был добавлен в избранное')
                a = True
                break
        else:
            if a is True:
                break
    else:
        print(f'К сожалению фильма с названием "{favorite_film}" не найдено')

    repeat = input('\nХотите проверить еще фильм? да/нет : ')
    if repeat.lower() == "нет":
        break
    elif repeat.lower() != "да":
        print('Ошибка выбора. Видимо вы хотите добавить еще фильмов!')

print('\nВы добавили в избранное: ')
for i in favorite_film_list:
    print(i)

#да, знаю, замудрил, но решил уж сделать проверку по максимуму.
#Расстояние Левенштейна узнал из интенсива по написанию телеграмм бота, решил что тут очень к месту его применение