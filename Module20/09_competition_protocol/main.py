def input_result(count):
    protocol.append(input("{} запись: ".format(count)).split())
    if protocol[count-1][0].isdigit() is False:
        print("Количество очков может быть только числовым значением! Попробуйте ввести снова. ")
        protocol.pop(count - 1)
        input_result(count)
    elif len(protocol[count-1]) != 2:
        print("Данные не соответствуют форме ввода. Вводите о форме (Результат Имя) через пробел. Попробуйте ввести снова. ")
        protocol.pop(count - 1)
        input_result(count)
    protocol[count-1][0] = int(protocol[count-1][0])




protocol = []
final_result = []

# вносим данные по каждой игре
N = int(input("Сколько записей вносится в протокол? "))
print("Записи (результат и имя): ")
for count in range(1, N+1):
    input_result(count)

# для теста создал готовый список
# protocol =[[69485, 'Jack'], [95715, 'qwerty'], [95715, 'Alex'], [83647, 'M'], [197128, 'qwerty'], [95715, 'Jack'], [93289, 'Alex'], [95715, 'Alex'], [95715, 'M']]


# из общего протокола отбираем максимальные очки для каждого участника, указывая сколько максимум очков набирал в прошлых играх
for score, name in protocol:
    if len(final_result) > 0:
        for score_final, name_final, score_previous in final_result:
            i = final_result.index([score_final, name_final, score_previous])
            if score > score_final and name == name_final:
                final_result[i] = [score, name, score_final]
                break
            elif score <= score_final and name == name_final:
                break
        else:
            final_result.append([score, name, score_final])
    else:
        final_result.append([score, name, 0])

final_result = sorted(final_result, reverse=True)


# сортировка методом пузырька для определения у кого предыдущий результат был больше
for run in range(len(final_result)-1):
    for n in range(len(final_result)-1):
        if final_result[n][0] == final_result[n+1][0]:
            if final_result[n][2] < final_result[n+1][2]:
                final_result[n], final_result[n+1] = final_result[n+1], final_result[n]

print("\nИтоги соревнований:")
# берем 3 значения из финального списка и печатаем
for score_final, name_final, score_previous in final_result[:3]:
    i = final_result.index([score_final, name_final, score_previous])
    print("{} место. {} ({})".format(i+1, name_final, score_final))
