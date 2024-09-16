def can_queen_move(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return True
    elif x1 == x2 or y1 == y2:
        return True
    elif abs(x1 - x2) == abs(y1 - y2):
        return True
    else:
        return False

def get_valid_coordinate(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 8:
                return value
            else:
                print("Помилка: координата повинна бути в діапазоні від 1 до 8.")
        except ValueError:
            print("Невірний ввід. Будь ласка, введіть ціле число.")

x1 = get_valid_coordinate("Введіть координату x1 (від 1 до 8): ")
y1 = get_valid_coordinate("Введіть координату y1 (від 1 до 8): ")
x2 = get_valid_coordinate("Введіть координату x2 (від 1 до 8): ")
y2 = get_valid_coordinate("Введіть координату y2 (від 1 до 8): ")

if can_queen_move(x1, y1, x2, y2):
    print(f"Ферзь може перейти з поля ({x1}, {y1}) на поле ({x2}, {y2}) за один хід.")
else:
    print(f"Ферзь НЕ може перейти з поля ({x1}, {y1}) на поле ({x2}, {y2}) за один хід.")
