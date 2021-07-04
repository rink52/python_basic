import random

N = int(input('Кол-во палок: '))
K = int(input('Кол-во бросков: '))

list_c = ["I" for _ in range(N)]

for throw in range(K):
    L = random.randint(1, N)
    R = random.randint(L, N)
    print(f'Бросок {throw+1}. Сбиты палки с номера {L} по номер {R}')
    for i in range(L-1, R):
        list_c[i] = '.'

print('\nРезультат: ', end='')
for i in list_c:
    print(i, end='')
