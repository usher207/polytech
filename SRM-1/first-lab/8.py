A = int(input("Введіть ціле число A: "))
B = int(input("Введіть ціле число B: "))

if A < B:

    for i in range(A + 1, B):
        print(i, end=' ')

    N = B - A - 1
    print(f"Кількість чисел N: {N}")
else:
    print("erorr: A > B")
