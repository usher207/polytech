class Employee:
    '''Клас для зберігання інформації про працівника.'''
    
    def __init__(self, name, age, position, pay):
        self.name = name
        self.age = age
        self.position = position
        self.pay = pay
    
    def print_details(self):
        '''Виводить інформацію про працівника.'''
        print(f"\nІм'я: {self.name}")
        print(f"Вік: {self.age} років")
        print(f"Посада: {self.position}")
        print(f"Заробітна плата: {self.pay} грн")
    
    def give_raise(self, amount):
        '''Підвищує зарплату на зазначену суму.'''
        self.pay += amount
        print(f"Зарплата {self.name} була підвищена на {amount} грн.")
    
    def change_position(self, new_position):
        '''Змінює посаду працівника.'''
        self.position = new_position
        print(f"{self.name} змінив посаду на {self.position}.")

def validate_age(age):
    '''Перевіряє, чи вік є дійсним цілим числом.'''
    if age.isdigit() and 0 < int(age) < 120:
        return int(age)
    else:
        raise ValueError("Вік має бути цілим числом між 1 і 120.")

def validate_pay(pay):
    '''Перевіряє, чи зарплата є дійсним числом.'''
    try:
        pay_float = float(pay)
        if pay_float >= 0:
            return pay_float
        else:
            raise ValueError("Зарплата не може бути від'ємною.")
    except ValueError:
        raise ValueError("Зарплата має бути дійсним числом.")

if __name__ == "__main__":
    try:
        name = input("Введіть ім'я працівника: ").strip()
        age_input = input("Введіть вік працівника: ").strip()
        age = validate_age(age_input)
        
        position = input("Введіть посаду працівника: ").strip()
        pay_input = input("Введіть зарплату працівника: ").strip()
        pay = validate_pay(pay_input)

        employee1 = Employee(name, age, position, pay)
        
        employee1.print_details()
        
        raise_amount = float(input("Введіть суму для підвищення зарплати: "))
        employee1.give_raise(raise_amount)
        
        new_position = input("Введіть нову посаду: ").strip()
        employee1.change_position(new_position)
        
        employee1.print_details()
    
    except ValueError as e:
        print(f"Помилка: {e}")
