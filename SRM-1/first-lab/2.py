import math
import math

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Будь ласка, введіть додатне число.")
        except ValueError:
            print("Невірний ввід. Спробуйте ще раз.")

a = get_positive_integer("Введіть додатне значення a: ")
b = get_positive_integer("Введіть додатне значення b: ")
с = math.sqrt(a * b)
print(f"Середнє геометричне чисел {a} та {b} = {с}")