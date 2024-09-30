import numpy as np

a = np.array([float(i) for i in range(1, 101)]) 

b = a.reshape(10, 10)

b_string = np.array2string(b, separator=', ')

print("Одномірний масив a:")
print(a)

print("\nМатриця b розміром 10x10:")
print(b_string)
