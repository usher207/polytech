x1 = int(input("Введіть координату x1: "))
y1 = int(input("Введіть координату y1: "))
x2 = int(input("Введіть координату x2: "))
y2 = int(input("Введіть координату y2: "))

len_x = (x2 - x1)
len_y = (y2 - y1)

s = len_x * len_y
p = 2 * (len_x + len_y)

print(f"S= {s}")
print(f"P= {p}")
