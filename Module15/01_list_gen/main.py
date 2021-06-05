N = int(input('Введите конечное число: '))
number_list = []
for number in range(1,N+1):
    if number % 2 != 0:
        number_list.append(number)
print(number_list)