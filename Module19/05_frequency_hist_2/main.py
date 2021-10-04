text = "Здесь что-то написано"

origin_frequency = {}
invertion_frequency = {}

# Заполняем первый словарь и печатаем
for sym in text:
    if sym in origin_frequency:
        origin_frequency[sym] = origin_frequency.get(sym) + 1
    else:
        origin_frequency[sym] = 1

print("\nОригинальный словарь частот:")
for key_dict_origin_frequency_print in origin_frequency:
    print(key_dict_origin_frequency_print, end=' : ')
    print(origin_frequency[key_dict_origin_frequency_print])

#Определяем максимальное значение частоты и заполняем второй словарь
# ключами от 1 до нашего максимального, со значениями в виде списка
for i in range(1, max(origin_frequency.values()) + 1):
    invertion_frequency[i] = []

# Заполняем списки второго словаря согласно ключам,
# сравнивая ключи второго словаря со значениями первого и печатаем
for key_dict_origin_frequency in origin_frequency:
    for key_dict_invertion_frequency in invertion_frequency:
        if origin_frequency[key_dict_origin_frequency] == key_dict_invertion_frequency:
            invertion_frequency[key_dict_invertion_frequency].append(key_dict_origin_frequency)

print("\nИнвертированный словарь частот:")
for key_dict_invertion_frequency_print in invertion_frequency:
    print(key_dict_invertion_frequency_print, end = ' : ')
    print(invertion_frequency[key_dict_invertion_frequency_print])


