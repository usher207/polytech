from datetime import datetime

def sort_by_birthdate(tup):
    def get_birthdate(item):
        return datetime.strptime(item[1], "%d.%m.%Y")  

    sorted_tuple = tuple(sorted(tup, key=get_birthdate))
    
    return sorted_tuple

students = (
    ["Іванов Іван Іванович", "15.04.2000"],
    ["Петров Петро Петрович", "23.02.1999"],
    ["Сидоренко Сидір Сидорович", "10.12.2001"],
    ["Коваленко Оксана Іванівна", "01.01.1998"]
)

sorted_students = sort_by_birthdate(students)

print("Сортований кортеж студентів за датами народження:")
for student in sorted_students:
    print(student)
