cell_list = []
bad_effectiveness_cell = []
N = int(input('Кол-во клеток: '))
for i in range(1, N+1):
    effectiveness_cell = int(input(f'Эффективность {i} клетки: '))
    cell_list.append(effectiveness_cell)
    if effectiveness_cell < i:
        bad_effectiveness_cell.append(effectiveness_cell)
#        print(f'\nКлетка c рангом {i} и эффективностью {effectiveness_cell} не подходит\n')

print('\nНеподходящие значения: ', end='')
for i in bad_effectiveness_cell:
    print(i, end=' ')


#Я бы вывод результатов сделал как в закомментированной строке. Но раз в задании указано так, сделал как требуется.
#также добавил запись значений в общий список, хотя для выполнения этого задания это не нужно.
#еще хорошо бы было сделать так чтоб в строке неподходящие значения выводились не только сами значения, но и индекс(ранг) клетки.