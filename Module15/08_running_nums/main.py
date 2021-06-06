shift = int(input('Сдвиг: '))

element_list = [1, 2, 3, 4, 5]
shift_element_list = []

for i in range(len(element_list)):
    if i+1 <= shift:
        shift_element_list.append(element_list[len(element_list)-shift+i])
    else:
        shift_element_list.append(element_list[i-shift])


print('Изначальный список: ', element_list)
print('Сдвинутый список: ', shift_element_list)


# for i in range(len(element_list)):
#     if i + shift < len(element_list):
#         shift_element_list[i+shift] = element_list[i]
#     elif i + shift > len(element_list):
#         shift_element_list[(i+shift)-len(element_list)] = element_list[i]
#     else:
#         shift_element_list[0] = element_list[i]
#сначала начал делать этим методом, но уперся в то, что
#во-первых тут нужно создавать изначально измененный список с такой же длинной как и изначальный
#а во-вторых несоответствие условиям задания по количеству присваиваний
