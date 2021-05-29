import math

print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
radius = float(input('Введите радиус: '))

if math.sqrt(x**2 + y**2) > radius:
    print('Монетки в области нет')
else:
    print('Монетка где-то рядом')

