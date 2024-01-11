#Build a hotel reservation system with classes for rooms, guests, and reservations.Implement methods for checking room availability, booking rooms, and generatinginvoices.
class Room:
    def __init__(self, room_number, capacity, price_per_night):
        self.room_number = room_number
        self.capacity = capacity
        self.price_per_night = price_per_night
        self.is_booked = False

class Guest:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Reservation:
    def __init__(self, guest, room, check_in_date, check_out_date):
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def calculate_total_cost(self):
        num_nights = (self.check_out_date - self.check_in_date).days
        return num_nights * self.room.price_per_night

class Hotel:
    def __init__(self):
        self.rooms = []
        self.reservations = []

    def add_room(self, room_number, capacity, price_per_night):
        room = Room(room_number, capacity, price_per_night)
        self.rooms.append(room)

    def display_available_rooms(self):
        available_rooms = [room for room in self.rooms if not room.is_booked]
        print("Available Rooms:")
        for room in available_rooms:
            print(f"Room {room.room_number} - Capacity: {room.capacity}, Price per Night: ${room.price_per_night}")

    def book_room(self, guest, room_number, check_in_date, check_out_date):
        room = next((r for r in self.rooms if r.room_number == room_number and not r.is_booked), None)

        if room:
            reservation = Reservation(guest, room, check_in_date, check_out_date)
            self.reservations.append(reservation)
            room.is_booked = True
            print(f"Room {room.room_number} booked successfully.")
            return reservation
        else:
            print("Selected room is not available for booking.")
            return None

# Example usage with user input:
hotel = Hotel()

# Adding rooms to the hotel
hotel.add_room(101, 2, 100)
hotel.add_room(102, 4, 150)
hotel.add_room(103, 3, 120)

# Getting user input for guest details
guest_name = input("Enter your name: ")
guest_email = input("Enter your email: ")
guest_phone = input("Enter your phone number: ")

# Creating a guest object
guest = Guest(guest_name, guest_email, guest_phone)

# Displaying available rooms
hotel.display_available_rooms()

# Getting user input for room booking
room_number = int(input("Enter the room number you want to book: "))
check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
check_out_date = input("Enter check-out date (YYYY-MM-DD): ")

# Creating a reservation
reservation = hotel.book_room(guest, room_number, check_in_date, check_out_date)

# Displaying reservation details
if reservation:
    print("\nReservation Details:")
    print(f"Guest: {reservation.guest.name}")
    print(f"Room: {reservation.room.room_number}")
    print(f"Check-in: {reservation.check_in_date}")
    print(f"Check-out: {reservation.check_out_date}")
    print(f"Total Cost: ${reservation.calculate_total_cost()}")
