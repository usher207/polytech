import numpy as np

def merge_arrays(array1, array2):
    """Функція для злиття двох впорядкованих масивів в третій."""
    merged_array = np.empty(len(array1) + len(array2), dtype=array1.dtype)  
    i = j = k = 0  

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            merged_array[k] = array1[i]
            i += 1
        else:
            merged_array[k] = array2[j]
            j += 1
        k += 1

    while i < len(array1):
        merged_array[k] = array1[i]
        i += 1
        k += 1

    while j < len(array2):
        merged_array[k] = array2[j]
        j += 1
        k += 1

    return merged_array

def insert_elements(array1, array2):
    """Функція для вставлення елементів другого масиву в перший."""
    for element in array2:
        position = 0
        while position < len(array1) and array1[position] < element:
            position += 1

        array1 = np.insert(array1, position, element)

    return array1

def get_sorted_array_input(prompt):
    """Функція для введення впорядкованого масиву з валідацією."""
    while True:
        input_numbers = input(prompt)
        try:
            
            numbers = [int(num) for num in input_numbers.split(",")]
            
            if all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1)):
                return np.array(numbers)
            else:
                print("Помилка: масив повинен бути впорядкований за зростанням.")
        except ValueError:
            print("Помилка: будь ласка, введіть тільки цілі числа, розділені комами.")

array1 = get_sorted_array_input("Введіть перший впорядкований масив (цілі числа, розділені комами): ")
array2 = get_sorted_array_input("Введіть другий впорядкований масив (цілі числа, розділені комами): ")

merged_result = merge_arrays(array1, array2)
print("Злитий масив:", merged_result)

inserted_result = insert_elements(array1.copy(), array2)
print("Після вставлення елементів другого масиву:", inserted_result)
