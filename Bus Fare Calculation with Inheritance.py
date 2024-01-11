#Create a Bus child class that inherits from the Vehicle class. The default farecharge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, weneed to add an extra 10% on full fare as a maintenance charge. So total fare forbus instance will become the final amount = total fare + 10% of the total fare.
class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def calculate_fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def calculate_fare(self):
        base_fare = super().calculate_fare()
        maintenance_charge = 0.1 * base_fare
        total_fare = base_fare + maintenance_charge
        return total_fare

# User input for seating capacity
seating_capacity = int(input("Enter seating capacity for the vehicle: "))

# Creating instances of Bus and Vehicle
vehicle_instance = Vehicle(seating_capacity)
bus_instance = Bus(seating_capacity)

# Calculating and displaying fare for both instances
print(f"Vehicle Fare: ${vehicle_instance.calculate_fare()}")
print(f"Bus Fare: ${bus_instance.calculate_fare()}")
