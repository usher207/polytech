def get(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Невірний ввід. Будь ласка, введіть ціле число.")

x1 = get("Введіть координату x1: ")
y1 = get("Введіть координату y1: ")
x2 = get("Введіть координату x2: ")
y2 = get("Введіть координату y2: ")

len_x = abs(x2 - x1)
len_y = abs(y2 - y1)

s = len_x * len_y
p = 2 * (len_x + len_y)

print(f"S= {s}")
print(f"P= {p}")