def configurate_tuple(data, random_elem):
    global new_tuple
    new_tuple = ()
    if random_elem not in data:
        return new_tuple
    else:
        new_tuple += (random_elem,)
        for elem in data[data.index(random_elem)+1: ]:
            if elem == random_elem:
                new_tuple += (elem,)
                break
            else:
                new_tuple += (elem,)

    return new_tuple


# так как явно не указано из чего кортеж и какой элемент, поэтому запрашиваем строку и переводим в кортеж

data = tuple(input("Введите данные: "))
random_elem = input("Введите элемент: ")
configurate_tuple(data, random_elem)
print(new_tuple)