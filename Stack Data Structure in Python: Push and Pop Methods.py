#Write a Python program to create a class representing a stack data structure.Include methods for pushing and popping elements.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop.")

    def is_empty(self):
        return len(self.items) == 0

# Example usage with user input:
stack = Stack()

while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        element = input("Enter the element to push: ")
        stack.push(element)
        print(f"{element} pushed to the stack.")
    elif choice == '2':
        popped_element = stack.pop()
        if popped_element is not None:
            print(f"Popped element: {popped_element}")
    elif choice == '3':
        print("Quitting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
