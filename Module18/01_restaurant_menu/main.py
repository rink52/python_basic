parsing_menu = 'утиное филе;фланк-стейк;банановый пирог;плов'

print('Доступное меню: ', parsing_menu)

print('На данный момент в меню есть: ', parsing_menu.replace(';', ', '))

#или так
# menu = parsing_menu.split(';')
# print(', '.join(menu))

