students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

# полный список интересов всех студентов, а также общую длину всех фамилий студентов
def full_interests_and_len_surname(students):
    full_interests = []
    full_len_surname = 0
    for key, values in students.items():
        full_interests += values["interests"]
        full_len_surname += len(values["surname"])
    return set(full_interests), full_len_surname        #set() позволит убрать повторяющиеся значения

#Вывести на экран список пар “айди студента - возраст”
for i, data in students.items():
    print("id:", i, "- Возраст:", data['age'])

#функция вызывается, и все возвращаемые значения "распаковываются" в отдельные переменные,
# которые затем выводятся на экран.
full_interests, full_len_surname = full_interests_and_len_surname(students)
print("Все интересы: ", full_interests, "\nДлинна всех фамилий: ", full_len_surname)


