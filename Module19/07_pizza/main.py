base = {}
N = int(input("Введите кол-во заказов: "))

for i in range(1, N+1):
    print('{} заказ: '.format(i), end='')
    base[i] = input().split()
    base[i][2] = int(base[i][2])

base_client = {}

for number_orders, orders in base.items():
    if orders[0] not in base_client:
        base_client[orders[0]] = {orders[1]: orders[2]}
    else:
        for name, base_order in base_client.items():
            if name == orders[0]:
                for pizza, count in base_order.items():
                    if pizza == orders[1]:
                        base_client[orders[0]][orders[1]] += orders[2]
                        break
                    else:
                        base_client[orders[0]][orders[1]] = orders[2]
                        break

for names, pizzas in sorted(base_client.items()):
    print('{} : '.format(names))
    for pizza, count in sorted(pizzas.items()):
        print("\t{} : {}".format(pizza, count))

