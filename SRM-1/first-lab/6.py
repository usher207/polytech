x = int(input("Введіть координату x (від 1 до 8): "))
y = int(input("Введіть координату y (від 1 до 8): "))

if x < 1 or x > 8 or y < 1 or y > 8:
    print("Координати повинні бути в діапазоні від 1 до 8.")
else:
    if (x + y) % 2 != 0:
        print(f"Поле з координатами ({x}, {y}) є білим.")
    else:
        print(f"Поле з координатами ({x}, {y}) є чорним.")