def input_coordinate(x):
    a = [0] * x
    for i in range(x):
        is_coordinate = False
        while not is_coordinate:
            try:
                number = float(input(f"Введите {i+1} координату: "))
                a[i] = number
                is_coordinate = True
                if a[i] == 0:
                    is_coordinate = False
                    print("Координата не должно быть равна 0 ")
            except ValueError:
                print("не корректный ввод")
    return a


def check_coordinate(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f"Точка находится в {text} четверти плоскости")


coordinate = input_coordinate(2)
check_coordinate(coordinate)