#Create a base class called “Animal” and two subclasses, “Dog” and “Cat.” Addmethods and attributes specific to each subclass.
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass  # Abstract method

class Dog(Animal):
    def __init__(self, breed):
        super().__init__("Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, color):
        super().__init__("Cat")
        self.color = color

    def make_sound(self):
        return "Meow!"

# Example usage:
dog_breed = input("Enter the dog's breed: ")
cat_color = input("Enter the cat's color: ")

dog = Dog(dog_breed)
cat = Cat(cat_color)

print(f"The {dog.species} makes sound: {dog.make_sound()}")
print(f"The {cat.species} makes sound: {cat.make_sound()}")
