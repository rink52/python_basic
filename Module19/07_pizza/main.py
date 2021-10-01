base = {}
base_client = {}

N = int(input("Введите кол-во заказов: "))

for i in range(1, N+1):
    print('{} заказ: '.format(i), end='')
    base[i] = input().split()
    base[i][2] = int(base[i][2])
    if base[i][0] not in base_client:
        base_client[base[i][0]] = {base[i][1]: base[i][2]}
    else:
        for name, base_order in base_client.items():
            if name == base[i][0]:
                for pizza, count in base_order.items():
                    if pizza == base[i][1]:
                        base_client[base[i][0]][base[i][1]] += base[i][2]
                        break
                    else:
                        base_client[base[i][0]][base[i][1]] = base[i][2]
                        break


for names, pizzas in sorted(base_client.items()):
    print('{} : '.format(names))
    for pizza, count in sorted(pizzas.items()):
        print("\t{} : {}".format(pizza, count))

