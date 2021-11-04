def add_contact():
    name = input("Введите Фамилию и Имя\n: ")
    if name in phonebook:
        print("Этот человек уже есть в списке! ")
        return
    number = input("Введите номер телефона\n: ")
    for key, value in phonebook.items():
        if number == value:
            print("С этим номером уже записан контакт: '{}'".format(key))
            return
    phonebook[name] = number

def search_contact():
    name = input("Введите Фамилию для поиска\n: ")
    for contact, number in phonebook.items():
        if name.lower() in str(contact).lower():
            print(contact, " : ", number)

def print_phonebook():
    print("\nВаша записная книжка: ")
    for contact, number in phonebook.items():
        print(contact, " : ", number)


phonebook = {"Петров Иван": 89996665522,
             "Петрова Светлана": 89996665523,
             "Иванов Степан": 89995556633,
             "Смирнова Дарья": 89994443333
             }
while True:
    action = input("\nВыберите, что вы хотите совершить:"
                   "\n1. - добавить контакт"
                   "\n2. - найти человека"
                   "\n3. - показать записную книжку"
                   "\n: "
                   )
    if action == "1":
        add_contact()
        print_phonebook()
    elif action == "2":
        search_contact()
    elif action == "3":
        print_phonebook()
    else:
        print("Ошибка выбора, попробуйте снова\n")

