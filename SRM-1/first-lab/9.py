def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Помилка: число повинно бути більше 0.")
        except ValueError:
            print("Невірний ввід. Будь ласка, введіть ціле число.")

N = get_positive_integer("Введіть ціле число N (N > 0): ")

reversed_N = 0

while N > 0:
    last_digit = N % 10
    reversed_N = reversed_N * 10 + last_digit
    N = N // 10

print(f"Зворотне число: {reversed_N}")
