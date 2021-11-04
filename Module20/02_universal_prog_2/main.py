def is_prime(n):
  if n < 2:
      return False
  elif n in (2, 3, 5, 7):
      return True
  else:
    for i in range(2, 8):
        if n % i != 0:
            continue
        else:
            return False
    else:
        return True

def return_elem_index_prime(data, decrypt_list):
    for index, value in enumerate(data):
        if is_prime(index) is True:
            decrypt_list.append(value)
    return decrypt_list

# в задании было сказано чтобы в функции был только return,
# придумал только такой костыль, но как основной вариант оставлять не стал
# def list_generation(data, decrypt_list):
#     return return_elem_index_prime(data, decrypt_list)


decrypt_list = []
data = [100, 200, 300, 'буква', 0, 2, 'а']

print(return_elem_index_prime(data, decrypt_list))

# print(list_generation(data, decrypt_list))


