import numpy as np

matrix = np.random.randint(1, 101, size=(10, 10))

print("Матриця:")
print(matrix)

max_in_columns = np.max(matrix, axis=0)

min_in_columns = np.min(matrix, axis=0)

max_in_rows = np.max(matrix, axis=1)

min_in_rows = np.min(matrix, axis=1)

print("\nНайбільші елементи стовпців:")
print(max_in_columns)

print("\nНайменші елементи стовпців:")
print(min_in_columns)

print("\nНайбільші елементи рядків:")
print(max_in_rows)

print("\nНайменші елементи рядків:")
print(min_in_rows)
