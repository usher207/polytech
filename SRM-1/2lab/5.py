import numpy as np
import random

def RandomArray(N):
    """Функція, що генерує масив з унікальними випадковими цілими числами від 1 до N."""
    random_numbers = []  

    while len(random_numbers) < N:
        num = random.randint(1, N)
        
        if random_numbers.count(num) == 0:
            random_numbers.append(num)

    return np.array(random_numbers)

while True:
    try:
        N = int(input("Введіть ціле число N (більше 0): "))
        if N > 0:
            break
        else:
            print("Помилка: N повинно бути більшим за 0.")
    except ValueError:
        print("Помилка: будь ласка, введіть ціле число.")

result_array = RandomArray(N)

print("Випадковий масив:", result_array)
