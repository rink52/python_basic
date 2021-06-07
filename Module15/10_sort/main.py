element_list = [1, 4, -3, 0, 10]
print('Изначальный список: ', element_list)

for i_one in range(len(element_list)):
    for i_two in range(i_one, len(element_list)):
        if element_list[i_two] < element_list[i_one]:
            element_list[i_one], element_list[i_two] = element_list[i_two], element_list[i_one]

# element_list.sort()
print('\nОтсортированный список: ', element_list)
