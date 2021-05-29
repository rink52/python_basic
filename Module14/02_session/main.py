print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))

if x1 == x2:
    print("Данная прямая параллельна оси OY, а ее уравнение можно записать в виде:")
    print("x = ", x1)

elif y1 == y2:
    print("Данная прямая параллельна оси OX, а ее уравнение можно записать в виде:")
    print("y = ", y1)

elif x1 == x2 and y1 == y2:
    print("Введенные координаты обозначают одну точку.")

else:
    x_diff = x1 - x2
    y_diff = y1 - y2
    k = y_diff / x_diff
    b = y2 - k * x2
    print("Уравнение прямой, проходящей через эти точки:")
    if b > 0:
        print("y = ", k, "* x + ", b)
    elif b < 0:
        print("y = ", k, "* x - ", b)
    else:
        print("y = ", k, "* x")

