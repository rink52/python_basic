shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
count_product = 0
summ = 0

product = input('Название детали:  ')

for i in shop:
        if i[0] == product.lower():
                count_product += 1
                summ += i[1]

print(f'Кол-во деталей - {count_product} шт.')
print(f'Общая стоимость -  {summ} руб.')


