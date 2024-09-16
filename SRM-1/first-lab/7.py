x1 = int(input("Введіть координату x1 (від 1 до 8): "))
y1 = int(input("Введіть координату y1 (від 1 до 8): "))
x2 = int(input("Введіть координату x2 (від 1 до 8): "))
y2 = int(input("Введіть координату y2 (від 1 до 8): "))

if (x1 < 1 or x1 > 8 or y1 < 1 or y1 > 8 or 
    x2 < 1 or x2 > 8 or y2 < 1 or y2 > 8):
    print("Координати повинні бути в діапазоні від 1 до 8.")
else:
    if x1 == x2 or y1 == y2 or abs(x2 - x1) == abs(y2 - y1):
        print(f"Ферзь може перейти з поля ({x1}, {y1}) на поле ({x2}, {y2}) за один хід.")
    else:
        print(f"Ферзь не може перейти з поля ({x1}, {y1}) на поле ({x2}, {y2}) за один хід.")