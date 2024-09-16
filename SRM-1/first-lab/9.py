def get(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Невірний ввід. Будь ласка, введіть ціле число.")

N = get("Введіть ціле число N: ")

sign = '-' if N < 0 else ''
N = str(abs(N))  

reversed_N = N[::-1]

result = sign + reversed_N
print(f"Зворотне число: {result}")
