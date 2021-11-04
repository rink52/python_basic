original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []
for one_elem, two_elem in zip(original_list[::2], original_list[1::2]):
    new_list.append((one_elem, two_elem))
print(new_list)


print([*map(tuple, zip(original_list[::2], original_list[1::2]))])
