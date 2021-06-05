def revers_number(number):
    str_number = str(number)
    partition_number = str_number.partition('.')
    int_revers_number = (partition_number[0])[::-1]
    remainder_revers_number = (partition_number[2])[::-1]
    revers_number = float(int_revers_number + partition_number[1] + remainder_revers_number)
    return revers_number


first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))

revers_first_number = revers_number(first_number)
revers_second_number = revers_number(second_number)

summ_number = revers_first_number + revers_second_number

print('\nПервое число наоборот: ', revers_first_number)
print('Второе число наоборот: ', revers_second_number)
print('\nСумма: ', summ_number)


# сначала думал сделать через срез, но понял что количество цифр модет быть разное,
# а в задании четко не указано сколько знаков до и после точки.
# затем думал решить математически, разделяя через int и % на целое число и остаток,
# но в этом случае количество зноков в остатке увеличивалось,
# и нужно было либо сначало проверять через строку количество знаков после точки через срез до символа "."
# а после округлять до этого знака. Но это тоже очень сложный код
# Нашел способ через разделение строки на несколько значений в кортеж по символу разделителю,
# получилось красиво. Но мне кажется что есть более простой способ решения?.

