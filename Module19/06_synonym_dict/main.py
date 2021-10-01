while True:
    dict_words = {}
    quantity = int(input("Введите количество пар слов: "))
    for i in range(1, quantity + 1):
        print("{} пара: ".format(i), end='')
        a = []
        b = []
        a = input().lower().split(" ")
        for element in a:
            if element.isalpha() is True:       # сначала хотел сделать по False удаление из "а", но тогда цикл переставал работать,
                b.append(element)               # так как индексы менялись. Пришлось выкручиваться с двумя списками.
        if len(b) != 2:
            print("Ошибка ввода, начните сначала\n")
            break
        dict_words[b[0]] = b[1]
    else:
        while True:
            word = input("\nВведите слово: ").lower()
            if dict_words.get(word) is not None:
                print("Синоним: {}".format(dict_words[word]))
            elif word in dict_words.values():
                for i in dict_words:
                    if dict_words[i] == word:
                        print("Синоним: {}".format(i))
            else:
                print("Такого слова в словаре нет.")


