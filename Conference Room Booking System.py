#Create a conference room booking system with classes for rooms, reservations,and users. Include methods for checking room availability, booking time slots, andsending notifications.
from datetime import datetime, timedelta

class Room:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity
        self.reservations = {}

    def check_availability(self, start_time, end_time):
        for reserved_start, reserved_end in self.reservations.values():
            if start_time < reserved_end and end_time > reserved_start:
                return False
        return True

    def book_room(self, user, start_time, end_time):
        if self.check_availability(start_time, end_time):
            reservation_id = len(self.reservations) + 1
            self.reservations[reservation_id] = (start_time, end_time, user)
            return reservation_id
        else:
            return None

    def display_reservations(self):
        print(f"Reservations for Room {self.room_number}:")
        for reservation_id, (start_time, end_time, user) in self.reservations.items():
            print(f"Reservation {reservation_id}: {user} - {start_time} to {end_time}")

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class ConferenceRoomBookingSystem:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room_number, capacity):
        self.rooms[room_number] = Room(room_number, capacity)

    def add_user(self, user_id, name):
        return User(user_id, name)

    def book_conference_room(self, room_number, user, start_time, end_time):
        if room_number in self.rooms:
            room = self.rooms[room_number]
            reservation_id = room.book_room(user.name, start_time, end_time)
            if reservation_id is not None:
                print(f"Room {room_number} booked successfully. Reservation ID: {reservation_id}")
            else:
                print("Room is not available for the specified time.")
        else:
            print("Invalid room number.")

# Example usage with user input:
booking_system = ConferenceRoomBookingSystem()

# Add rooms
booking_system.add_room(101, 10)
booking_system.add_room(102, 15)

# Add users
user1 = booking_system.add_user(1, "Alice")
user2 = booking_system.add_user(2, "Bob")

# Book conference room with user input
room_number = int(input("Enter room number: "))
start_time_str = input("Enter start time (YYYY-MM-DD HH:MM): ")
end_time_str = input("Enter end time (YYYY-MM-DD HH:MM): ")

start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")

booking_system.book_conference_room(room_number, user1, start_time, end_time)
booking_system.book_conference_room(room_number, user2, start_time, end_time)

# Display reservations
for room in booking_system.rooms.values():
    room.display_reservations()
