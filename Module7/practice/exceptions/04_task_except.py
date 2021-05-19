# Даны два уравнения прямых вида у=kx+b и виде строки. Проверить, пересекаются ли данные прямые?
# Примеры уравнений: "y = 2x + 4"  "y = -12x -12"

# Проверьте входные данные на корректность

def equation_input():
    while True:
        equation = input("Ввведите уравнение видя y = kx + b: ")
        eq_lst = equation.split()
        try:
            if eq_lst[0] != "y" or eq_lst[1] != "=" or not eq_lst[2].endswith("x") or eq_lst[3] != "+" or len(
                    eq_lst) != 5:
                raise ValueError
            k = eq_lst[2].rstrip("x")
            if k == '':
                k = 1
            elif k == '-':
                k = -1
            else:
                k = float(k)
            b = float(eq_lst[4])
            break
        except ValueError:
            print("Неверный формат")
    return k, b


k1, b1 = equation_input()
k2, b2 = equation_input()

x_cross = round((b2 - b1) / (k1 - k2), 2)
y_cross = round(k1 * x_cross + b1, 2)
print(k1, b1)
print(k2, b2)
print(f"Координаты точки пересечения прямых равны x={x_cross} y={y_cross}")
