#Create three classes, “Person,” “Employee,” and “Student.” Use multipleinheritance to create a class “PersonInfo” that inherits from both “Employee” and“Student.” Add attributes and methods specific to each class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Person: {self.name}, Age: {self.age}")

class Employee:
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}, Salary: {self.salary}")

class Student:
    def __init__(self, student_id, grade):
        self.student_id = student_id
        self.grade = grade

    def display_student_info(self):
        print(f"Student ID: {self.student_id}, Grade: {self.grade}")

class PersonInfo(Employee, Student):
    def __init__(self, name, age, employee_id, salary, student_id, grade):
        # Call constructors of base classes
        Employee.__init__(self, employee_id, salary)
        Student.__init__(self, student_id, grade)
        Person.__init__(self, name, age)

    def display_person_info(self):
        # Call methods of base classes
        Person.display_person_info(self)
        Employee.display_employee_info(self)
        Student.display_student_info(self)

# Get user input
name = input("Enter person's name: ")
age = int(input("Enter person's age: "))
employee_id = input("Enter employee ID: ")
salary = float(input("Enter salary: "))
student_id = input("Enter student ID: ")
grade = float(input("Enter grade: "))

# Create object of PersonInfo using user input
person_info = PersonInfo(name, age, employee_id, salary, student_id, grade)

# Display information
person_info.display_person_info()