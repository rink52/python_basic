text = "Здесь что-то написано"

a = {}
b = {}

# Заполняем первый словарь и печатаем
for sym in text:
    if sym in a:
        a[sym] = a.get(sym) + 1
    else:
        a[sym] = 1

print("\nОригинальный словарь частот:")
for key_dict_a_print in a:
    print(key_dict_a_print, end=' : ')
    print(a[key_dict_a_print])

#Определяем максимальное значение частоты и заполняем второй словарь
# ключами от 1 до нашего максимального, со значениями в виде списка
for i in range(1, max(a.values()) + 1):
    b[i] = []

# Заполняем списки второго словаря согласно ключам,
# сравнивая ключи второго словаря со значениями первого и печатаем
for key_dict_a in a:
    for key_dict_b in b:
        if a[key_dict_a] == key_dict_b:
            b[key_dict_b].append(key_dict_a)

print("\nИнвертированный словарь частот:")
for key_dict_b_print in b:
    print(key_dict_b_print, end = ' : ')
    print(b[key_dict_b_print])


