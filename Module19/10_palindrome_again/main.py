a = input("Введите строку: ")
b = dict.fromkeys(a, 0)

for i in a:
    b[i] = b.get(i) + 1

odd_sym = 0

for i in b:
    if b.get(i) % 2 != 0:
        odd_sym += 1

if odd_sym > 1:
    print("Сделать палиндром нельзя")
else:
    print("Можно сделать палиндром")