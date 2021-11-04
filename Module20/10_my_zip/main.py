def zip_func(first_object, second_object):
    for count in range(min(len(first_object), len(second_object))):
        print((first_object[count], second_object[count]), end=" ")


first = "abcd"
second = {10: 3, 20: 5, 30: "rf", 40: "ddd"}


print(zip(first, second))

zip_func(tuple(first), tuple(second))
