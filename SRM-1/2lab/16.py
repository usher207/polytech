def calculate_order_cost(price_list, order):
    inventory = {item[0].strip().lower(): [item[1], item[2]] for item in price_list}

    total_cost = 0

    for item, quantity in order:
        item = item.strip().lower()  

        if item not in inventory:
            return -2  

        available_quantity = inventory[item][1]
        if quantity > available_quantity:
            return -1  

       
        total_cost += inventory[item][0] * quantity
        inventory[item][1] -= quantity  

    return total_cost

price_list = [
    ["Хліб", 10, 100],
    ["Молоко", 20, 50],
    ["Яблука", 30, 200],
]

order = (
    ("хліб", 2),
    ("молоко", 1),
    ("яблука", 3),
)

result = calculate_order_cost(price_list, order)

if result >= 0:
    print("Вартість замовлення:", result)
else:
    if result == -1:
        print("Запитувана кількість товару перевищує наявну.")
    elif result == -2:
        print("Товару з таким найменуванням немає в прейскуранті.")
