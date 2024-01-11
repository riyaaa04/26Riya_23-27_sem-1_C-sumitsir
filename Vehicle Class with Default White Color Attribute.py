#Define a class attribute “color” with a default value white. i.e., Every Vehicleshould be white.
class Vehicle:
    color = "white"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}\n")

# Example usage:
make_input = input("Enter the make of the vehicle: ")
model_input = input("Enter the model of the vehicle: ")
year_input = input("Enter the year of the vehicle: ")

vehicle = Vehicle(make_input, model_input, year_input)
vehicle.display_details()
