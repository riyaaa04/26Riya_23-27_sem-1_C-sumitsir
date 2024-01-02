#Create a base class called “Vehicle” with a method called “drive.” Implement twosubclasses, “Car” and “Bicycle,” that inherit from “Vehicle” and override the “drive”method with their own implementations.
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        return "Generic vehicle driving method"

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def drive(self):
        return f"{self.brand} {self.model} is driving with {self.fuel_type} fuel"

class Bicycle(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model)
        self.type = type

    def drive(self):
        return f"{self.brand} {self.model} is cycling"

# Get user input for car details
car_brand = input("Enter the car brand: ")
car_model = input("Enter the car model: ")
car_fuel_type = input("Enter the car fuel type: ")

# Get user input for bicycle details
bicycle_brand = input("Enter the bicycle brand: ")
bicycle_model = input("Enter the bicycle model: ")
bicycle_type = input("Enter the bicycle type: ")

# Create objects of Car and Bicycle classes
car_obj = Car(car_brand, car_model, car_fuel_type)
bicycle_obj = Bicycle(bicycle_brand, bicycle_model, bicycle_type)

# Display the details and drive method for each vehicle
print("\nCar Details:")
print(f"Brand: {car_obj.brand}, Model: {car_obj.model}, Fuel Type: {car_obj.fuel_type}")
print(f"Drive: {car_obj.drive()}")

print("\nBicycle Details:")
print(f"Brand: {bicycle_obj.brand}, Model: {bicycle_obj.model}, Type: {bicycle_obj.type}")
print(f"Drive: {bicycle_obj.drive()}")