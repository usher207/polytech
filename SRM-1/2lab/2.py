import numpy as np

def create_array(*args):
    return np.array(args)

while True:
    input_numbers = input("Введіть цілі числа, розділені комами: ")

    try:
        numbers = [int(num) for num in input_numbers.split(",")]
        break  
    except ValueError:
        print("Помилка: будь ласка, введіть тільки цілі числа, розділені комами.")

result = create_array(*numbers)

print("Масив:", result)
