import numpy as np

a = np.array([float(i) for i in range(1, 101)])

a_reshaped = a.reshape(100, 1)

print("Оригінальний масив a (1x100):")
print(a)

print("\nПеретворений масив a (100x1):")
print(a_reshaped)

print("\nФорма оригінального масиву a:", a.shape)
print("Форма перетвореного масиву a:", a_reshaped.shape)
