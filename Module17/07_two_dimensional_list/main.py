cols = 3
rows = 4

list_number = [list(range(x, (rows * cols) + x - rows + 1, rows))
               for x in range(1, rows + 1)]

print(list_number)

