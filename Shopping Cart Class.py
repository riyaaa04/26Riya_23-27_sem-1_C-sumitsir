#Write a Python program to create a class representing a shopping cart. Includemethods for adding and removing items, and calculating the total price.
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity):
        if item in self.items:
            self.items[item]["quantity"] += quantity
        else:
            self.items[item] = {"price": price, "quantity": quantity}

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
        else:
            print(f"{item} not found in the cart.")

    def calculate_total_price(self):
        total_price = sum(item["price"] * item["quantity"] for item in self.items.values())
        return total_price

    def display_cart(self):
        print("Shopping Cart Contents:")
        for item, details in self.items.items():
            print(f"{item}: Quantity - {details['quantity']}, Price per unit - ${details['price']}")

# Example usage with user input:
cart = ShoppingCart()

while True:
    print("\n1. Add item to cart")
    print("2. Remove item from cart")
    print("3. View cart")
    print("4. Calculate total price")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        item = input("Enter item name: ")
        price = float(input("Enter price per unit: "))
        quantity = int(input("Enter quantity: "))
        cart.add_item(item, price, quantity)

    elif choice == '2':
        item_to_remove = input("Enter item to remove: ")
        cart.remove_item(item_to_remove)

    elif choice == '3':
        cart.display_cart()

    elif choice == '4':
        total_price = cart.calculate_total_price()
        print(f"Total Price: ${total_price}")

    elif choice == '5':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
