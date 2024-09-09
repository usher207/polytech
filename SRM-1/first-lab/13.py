first_name = input("Введіть своє ім'я: ")
last_name = input("Введіть своє прізвище: ")
phone_number = input("Введіть свій номер телефону: ")

if not first_name or not last_name or not phone_number:
    print("Не залишайте жодні поля порожніми")
else:
    print("Спасибі")


# v2.0
first_name = input("Введіть своє ім'я: ")
last_name = input("Введіть своє прізвище: ")
phone_number = input("Введіть свій номер телефону: ")

if first_name or last_name or phone_number:
    print("Спасибі")
else:
    print("Не залишайте всі поля порожніми")

# v2.1
first_name = input("Введіть своє ім'я: ")
last_name = input("Введіть своє прізвище: ")
phone_number = input("Введіть свій номер телефону (необов'язково): ")

if not first_name or not last_name:
    print("Не залишайте жодні поля порожніми")
else:
    print("Спасибі")
