container_list = []
i = 1

quantity_containers = int(input('Кол-во контейнеров: '))
for _ in range(quantity_containers):
    container_list.append(input('Введите вес контейнера: '))
new_container = int(input('Введите вес нового контейнера: '))

for ch in container_list:
    if int(ch) >= new_container:
        i += 1

print('Номер, куда встанет новый контейнер: ', i)
