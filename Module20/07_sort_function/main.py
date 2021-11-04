def sort_luple(tuple_number):
    for i in tuple_number:
       if type(i) is not int:
           print(tuple_number)
           break

    else:
        print(tuple(sorted(tuple_number)))

tuple_number = 1,5,56,8,4,6,4,5,4,5,45,5
sort_luple(tuple_number)
