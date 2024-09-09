array = list(map(int, input("Введіть елементи масиву через пробіл: ").split()))

average = sum(array) / len(array)

for i in range(len(array)):
    if array[i] > average:
        array[i] -= 18  

print("Масив після обробки:", array)
