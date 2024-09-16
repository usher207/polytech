str1 = "Hello, world!"
print(f"Оригінальний рядок: {str1}")

try:
    str1[7] = 'W'
except TypeError as e:
    print(f"Помилка: {e}")

str2 = " Python is awesome!"
combined_str = str1 + str2
print(f"Об'єднаний рядок: {combined_str}")

multiplied_str = str2 * 10
print(f"Рядок, розмножений 10 разів: {multiplied_str}")

insert_position = 1
modified_str = str1[:insert_position] + 'X' + str1[insert_position:]
print(f"Рядок після вставки символа 'X': {modified_str}")

new_str = str1[:7] + 'W' + str1[8:]
print(f"Новий рядок з одним зміненим символом: {new_str}")
