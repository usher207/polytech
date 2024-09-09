max_attempts = 5

for attempt in range(max_attempts):
    user_input = int(input("Введіть число: "))
    
    if user_input == 5:
        print("Молодець! Ви ввели правильне число.")
        break
else:
    print("Ви не ввели правильне число за 5 спроб.")
