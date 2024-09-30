class Student:
    '''Зберігає особисті дані студента, email, ім'я, телефон та інше.'''
    
    def __init__(self, name="John Doe", courses=None, phone_number="", email="", degree=""):
        if courses is None:
            courses = []
        self.name = name
        self.courses = courses
        self.phone_number = phone_number
        self.email = email
        self.degree = degree
        print("Створено об’єкт для " + name)

    def printDetails(self):

        print("Ім’я: ", self.name)
        print("Курси: ", self.courses)
        print("Телефон: ", self.phone_number)
        print("Email: ", self.email)
        print("Ступінь: ", self.degree)

    def enroll(self, course):
        self.courses.append(course)


student1 = Student("Mary", ["L548"], "123-456-7890", "mary@example.com", "Bachelor")
print("Уведіть курси, які вивчає", student1.name)

newcourse = input("Уведіть номер курсу або 'stop': ")
while newcourse != "stop":
    student1.enroll(newcourse)
    newcourse = input("Уведіть номер курсу або 'stop': ")

student1.printDetails()
