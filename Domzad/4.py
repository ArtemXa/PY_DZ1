def values_of_quarter():
    print("Введите целое число от 1 до 4 соответствующее номеру четверти")
    quarter = input()
    try:
        quarter = int(quarter)
    except:
        print('Введите целое число, а не буквы')
        values_of_quarter()
    if 0 < quarter <= 4:
        if quarter == 1:
            print("X ∈ (0, -∞); Y ∈ (0, ∞)")
        elif quarter == 2:
            print("X ∈ (0, ∞); Y ∈ (0, ∞)")
        elif quarter == 3:
            print("X ∈ (0, ∞); Y ∈ (0, -∞)")
        elif quarter == 4:
            print("X ∈ (0, -∞); Y ∈ (0, -∞)")
    else:
        print('Вы вышли за границы нужного интервала 1 - 4')


values_of_quarter()
