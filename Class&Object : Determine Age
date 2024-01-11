#Write a Python program to create a person class. Include attributes like name,country and date of birth. Implement a method to determine the person's age.
from datetime import date

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def calculate_age(self):
        today = date.today()
        birth_year = int(self.dob.split('-')[0])
        age = today.year - birth_year
        return age

# Get user input
name = input("Enter person's name: ")
country = input("Enter person's country: ")
dob = input("Enter person's date of birth (YYYY-MM-DD): ")

# Create Person object
person = Person(name, country, dob)

# Calculate and display age
age = person.calculate_age()
print(f"{person.name} is {age} years old.")
