a = int(input("Введіть ціле число a: "))
b = int(input("Введіть ціле число b: "))
c = int(input("Введіть ціле число c: "))

if a < b < c:
    print(f"a < b < c = true.")
else:
    print(f"a < b < c = false.")

if a > 0 or b > 0 or c > 0:
    print("atleast one >0 = true.")
else:
    print("atleast one >0 = false.")

positive_count = (a > 0) + (b > 0) + (c > 0)

if positive_count == 1:
    print("only one >0 = true.")
else:
    print("only one >0' = false.")
