#Create a Python class called “Car” with attributes like make, model, and year.Then, create an object of the “Car” class and print its details.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Car Details:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}")

# Get user input for car details
make = input("Enter the car make: ")
model = input("Enter the car model: ")
year = input("Enter the car year: ")

# Create a Car object
car_obj = Car(make, model, year)

# Display the details of the car
car_obj.display_details()
