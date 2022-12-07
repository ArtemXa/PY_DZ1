def input_numbers(input_text):
    is_weekend = False
    while not is_weekend:
        try:
            number = int(input(f"{input_text}"))
            is_weekend = True
        except ValueError:
            print("не корректный ввод")
    return number


def check_number(num):
    if 6 <= num <= 7:
        print("ДА")
    elif 0 < num < 6:
        print("НЕТ")
    else:
        print("ввели не правильное число")


num = input_numbers("Введите число: ")
check_number(num)
