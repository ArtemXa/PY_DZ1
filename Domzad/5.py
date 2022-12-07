def input_numbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_coordinate = False
        while not is_coordinate:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                is_coordinate = True
            except ValueError:
                print("Не целое число")
    return a


def calculate_distance(a, b):
    distance = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return distance


print("Введите координаты точки А")
pointA = input_numbers(2)
print("Введите координаты точки В")
pointB = input_numbers(2)

print(f"Длина отрезка: {format(calculate_distance(pointA, pointB), '.2f')}")
