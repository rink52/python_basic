goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for name_of_good, code_of_good in goods.items():

    len_dict = 0

    quantity = 0

    full_price = 0

    for good in store[code_of_good]:

        quantity += good.get('quantity')

        full_price += good.get('price') * good.get('quantity')

    print(" {} - {} шт, стоимость {}".format(name_of_good, quantity, full_price))


# for i in store:                                                                             # идем по ключам store
#     len_dict = 0
#     quantity = 0
#     full_price = 0
#     for n in store[i]:                                                                      # идем по спискам каждого товара
#         quantity += n.get('quantity')                                                       # считаем количество через получение значения по ключу
#         full_price += n.get('price') * n.get('quantity')                                    # считаем сумму через произведение значений цены и количества по ключу
#         if len(store[i]) - 1 > len_dict:                                                    # проверяем количество значений в списке если не одно то включаем счетчик
#             len_dict += 1
#         else:
#             goods_text = list(goods.keys())[list(goods.values()).index(i)]                  # считываем название товара
#             print(" {} - {} шт, стоимость {}".format(goods_text, quantity, full_price))     # выводим результат