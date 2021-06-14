N = int(input('Кол-во друзей: '))
K = int(input('Долговых расписок: '))

#создаем список пользователей с суммой их долгов
user = list(range(1, N+1))
summ_user = []
summ_all = []

for ch_users in user:
    summ_user.append(ch_users)
    summ_user.append(0)
    summ_all.append(summ_user.copy())
    summ_user.clear()

#создаем список расписок
owe_list = []
owe = []
for i in range(K):
    print(f'{i+1} расписка')
    owe.append(int(input('Кому: ')))
    owe.append(int(input('От кого: ')))
    owe.append(int(input('Сколько: ')))
    owe_list.append(owe.copy())
    owe.clear()

#проверяем все ли введенные данные были корректны, обнуляем некорректные
# хотел вначале удалять через .remove() но тогда некорректно отрабатывается в дальнейшем цикл.
# можно было бы сделать проверку на этапе ввода, но мне показалось так проще.
for i in owe_list:
    if i[0] > N or i[0] < 1 or i[1] > N or i[1] < 1 or i[0] == i[1]:
        print(f'Ошибочные расписки удалены')

        i[0] = 0
        i[1] = 0
print(owe_list)

# сравниваем списки пользователей и расписок
# находим совпадения и записываем значения в суммы пользователей
for i in owe_list:
    for ch_user in summ_all:
        if ch_user[0] == i[0]:
            ch_user[1] -= i[2]
        elif ch_user[0] == i[1]:
            ch_user[1] += i[2]

#выводим результат
print('\nБалланс друзей: ')
for i in summ_all:
    print(f'{i[0]} : {i[1]}')