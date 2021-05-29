N = int(input('Введите натуральное число: '))

for choise in range(2,N+1):
    if N % choise == 0:
        print('Наименьший делитель, отличный от единицы = ', choise)
        break