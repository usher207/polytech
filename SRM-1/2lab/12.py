import numpy as np

array = np.random.randint(-50, 50, size=(10)) 
print("Масив:")
print(array)

negative_sum = np.sum(array[array < 0])

print("\nСума від'ємних елементів масиву:")
print(negative_sum)
