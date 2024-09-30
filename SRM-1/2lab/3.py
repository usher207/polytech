import numpy as np

def sort_12(array):
    """Функція для сортування масиву за зростанням."""
    return np.sort(array)

def sort_21(array):
    """Функція для сортування масиву за спаданням."""
    return np.sort(array)[::-1] 

while True:
    input_numbers = input("Введіть цілі числа, розділені комами: ")

    try:
        numbers = [int(num) for num in input_numbers.split(",")]
        break 
    except ValueError:
        print("Помилка: будь ласка, введіть тільки цілі числа, розділені комами.")

array = np.array(numbers)

sorted_12 = sort_12(array)
sorted_21 = sort_21(array)

print("Відсортований масив за зростанням:", sorted_12)
print("Відсортований масив за спаданням:", sorted_21)
