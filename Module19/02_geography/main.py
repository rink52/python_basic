number = int(input('Кол-во стран: '))
maps = {}
for count in range(1, number+1):
    countries, *cities = input('{} страна: '.format(count)).split()
    maps[countries] = set(cities)
    print(maps)

for count in range(1,4):
    city = input("{} город: ".format(count))
    for country in maps:
        if city in maps[country]:
            print('Город {} расположен в стране {}.'.format(city, country))
            break
    else:
        print('По городу {} данных нет.'.format(city))


